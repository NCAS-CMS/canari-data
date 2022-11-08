import cf
from pathlib import Path
from datetime import datetime, timezone
from itertools import islice
import json
import unittest

from serialise_cf import serialise

def nice_time(timestamp):
    return  datetime.fromtimestamp(timestamp, tz=timezone.utc)

def get_cell_methods(f):
    """ 
    Extract what we need to know about cell methods
    """
    if cf.__version__ < '3.14.0':
        cmset = f.cell_methods()
        try:
            for k,cm in cmset.items():
                cms = str(cm)
                axes = f.coordinates(filter_by_axis=cm.axes)
                for i, kk in enumerate(axes):
                    sname = getattr(axes[kk],'standard_name',"")
                    cms = cms.replace(cm.axes[i],sname)
                return cms
        except Exception as err:
            return cms
    else:
        return f.cell_methods()

class CFIndex:

    def __init__(self, dirname, 
                    check_file_times=False, # this isn't implemented yet
                    duplicate_logfile=None, 
                    namechecks=None,
                    standard_and_long=None,
                    index_file='cfindex.json'):
        """ 
        Index all the files in a directory <dirname> by their standard names and long names
        so that all files associated with <standard_name>:<long_name> are listed in 
        response to a getitem.

        I.e. Usage:

            index = CFIndex(directory)
            print(index['air_temperature:some_funny_long_name'])

        There are other methods too:

            index.volume()


        There are a bunch of additional checks that are done during indexing, and logs
        are created for those if logfile names are provided.
        
        """

        # persisted
        self._indexed_by_name = {}
        self._files={}
        self._fields_by_domain = {}
        
        # not persisted
        self._duplicate_check = {}
        self._name_checks={}
        self._long_names=[]
  
        # and we're off:

        path=Path(dirname)
        self.index_file = path/index_file
        last_updated = path.stat().st_mtime

        files = path.glob('*.nc')
        reindex = True
        if self.index_file.exists():
            if self.index_file.stat().st_mtime  > last_updated:
                reindex=False
            revisit = []
            if check_file_times:
                for file in files: 
                    if file.stat().m_time > last_updated:
                        revisit.append(file)

        if not reindex and revisit != []:
            # reload and get all the good stuff from the last index
            print('Updating from old index is not implemented, so for now we need to rebuild the entire index')
            reindex=True

        if reindex:

            if duplicate_logfile is not None:
                duplog = open(duplicate_logfile,'w')
            if namechecks is not None:
                namelog = open(namechecks,'w')
                
            #test_limit = 10
            test_limit = None
    
            if test_limit is not None:
                files = islice(files,test_limit)
            else:
                files = files

            allfields = []
            nfiles = 0
            ndups = 0
            for f in files:
                self._files[str(f)] = {'size':f.stat().st_size}
                fields = cf.read(f)
                nfiles +=1
                dup = False
                for ff in fields:
                    # we have instances of people having the same standard name, but different long names ... 
                    std_name = getattr(ff,'standard_name', None)
                    long_name = getattr(ff,'long_name',None)
                    id = f'{std_name}:{long_name}'
                    if id == 'None:None':
                        id = ff.identity()
                    if std_name is not None:
                        if std_name in self._name_checks:
                            if long_name != self._name_checks[std_name]:
                                message = f'Ignoring name inconsistency {std_name}, {self._name_checks[std_name]}, {long_name}\n'
                                if namechecks is not None:
                                    namelog.write(message)
                                else:
                                    pass
                        else:
                            self._name_checks[std_name] = long_name
                    key = id, self._domain_summary(ff)
                    if std_name is not None and long_name is not None:
                        self._long_names.append([std_name, long_name, key, ff.units])
                    if key in self._duplicate_check:
                        if duplicate_logfile is not None:
                            duplog.write(f'Skipping duplicate file {f} - {key}\n')
                            duplog.write(f'Duplicates {self._duplicate_check[key]}\n--\n')
                        ndups +=1
                        dup = True
                        continue
                    else:
                        self._duplicate_check[key]=f
                        
                    if id in self._indexed_by_name:
                        self._indexed_by_name[id].append(f.name)
                    else:
                        self._indexed_by_name[id]=[f.name]
                if not dup:
                    allfields += fields
            afields = cf.aggregate(allfields) 
            for f in afields:
                print(f)
            print(f'Index of {path} contains:')
            print(f' - {len(self._indexed_by_name)} named items')
            print(f' - representing {len(afields)} cf fields')
            print(f' - in {nfiles} different nc files')    
            if ndups:
                print(f' - ignoring {ndups} duplicate files')       
            
            self.save()
            if duplicate_logfile is not None:
                duplog.close()
            if namechecks:
                namelog.close()
            if self._long_names and standard_and_long is not None:
                with open(standard_and_long,'w') as f:
                    for x in self._long_names:
                        f.write(str(x)+'\n')
        else:
            print('Using cached index')
            with open(self.index_file,'r') as f:
                x = json.load(f)
                self._indexed_by_name = x['index']
                self._files = x['files']

    def volume(self,months=12,simulations=40,years=150, scalefactor=None, units=1e9):
        """ Return expected volumes in GB

            Seveal options, the default is set up for CANARI, and returns the 
            expected volume for the entire directory, but if scalefactor=1,
            it will simply return the current volume.

            You can scale the result too, the default is 1e9 (ie. GB)

        """
        sum = 0
        if scalefactor is None:
            scalefactor = months*simulations*years
        for x,y in self._files.items():
            v = y['size']*scalefactor/units
            print(f'{x}: {round(v,1):,}')
            sum+=v
        print(f"total: {round(sum):,}")

    def save(self):
        with open(self.index_file,'w') as f:
            json.dump({'index':self._indexed_by_name,'files':self._files},f)

    def _domain_summary(self,f):
        """ For a given domain, get a domain summary """
        #FIXME: should be outer edge of bounds, and I am not sure about the coords and ancils, is that sufficient?
        coords = [serialise(cf.Data.concatenate([b.min(), b.max()])) for b in [a.data for k,a in f.domain.dimension_coordinates().items()]]
        ancils = [serialise(cf.Data.concatenate([b.min(), b.max()])) for b in [a.data for k,a in f.domain.auxiliary_coordinates().items()]] 
        bbox = coords+ancils
        methods = get_cell_methods(f)
        return json.dumps({'bbox':bbox, 'methods':methods})
        
    def __getitem__(self, key):
        return self._indexed_by_name[key]

    def get_fields(self, key, directory='/'):
        """ Return the fields corresponding to the key"""
        file_keys = self[key]
        fields = cf.read([Path(directory)/f for f in file_keys])
        return fields

class TestCFIndex(unittest.TestCase):

    def setUp(self):
        self.simdir = 'u-cn134-1fpf'
        self.target = f'{self.simdir}/19500101T0000Z'
        self.index = Path(self.target)/'cf-index.json'

    def tearDown(self):
        if self.index.exists():
            self.index.unlink()

    def testIndex(self):
        assert not self.index.exists()
        index = CFIndex(self.target,
                    duplicate_logfile='duplicates.log', 
                    namechecks='names.log',
                    standard_and_long='long_names.log' )

    def NOtestPersistence(self):
        assert not self.index.exists()
        index = CFIndex(self.target)
        index2 = CFIndex(self.target)


if __name__== "__main__":
    unittest.main()
   





            


