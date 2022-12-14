import cf

from pathlib import Path
from datetime import datetime, timezone
from itertools import islice
import json
import unittest

from domain_handling import DomainSummary 

def nice_time(timestamp):
    return  datetime.fromtimestamp(timestamp, tz=timezone.utc)


def name_match(f, key):
    """ For key = "standard_name:long_name" return true 
            if f.standard_name == standard_name and f.long_name == long_name
    """
    try:
        standard, long = tuple(key.split(':'))
    except:
        return False
    if standard in ["","None"]:
        standard = None
    if long in ["","None"]:
        return long
    if getattr(f,'standard_name',None) != standard:
        return False
    if getattr(f,'long_name', None) != long:
        return False
    return True


class CFIndex:

    def __init__(self, dirname, 
                    check_file_times=False, # this isn't implemented yet
                    duplicate_logfile=None, 
                    namechecks=None,
                    standard_and_long=None,
                    index_file='cfindex.json',
                    force_rebuild=False):
        """ 
        Index all the files in a directory <dirname> by their standard names and long names
        so that all files associated with <standard_name>:<long_name> are listed in 
        response to a getitem.

        I.e. Usage:

            index = CFIndex(directory)
            print(index['air_temperature:some_funny_long_name'])

        There are other methods too:

            index.volume()

            flds = index.get_fields('air_temperature:some_funny_long_name)

        There are a bunch of additional checks that are done during indexing, and logs
        are created for those if logfile names are provided.
        
        """

        # persisted
        self._indexed_by_name = {}
        self._files = {}
        self.dirname = dirname
        

        # not persisted
        self._duplicate_check = {}
        self._name_checks={}
        self._long_names=[]
        self._fields_by_domain = {}
  
        # and we're off:

        path=Path(dirname)
        self.index_file = path/index_file
        last_updated = path.stat().st_mtime
        files = path.glob('*.nc')


        reindex = True
        if not force_rebuild: 
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
                    key = id, str(DomainSummary(ff)) 
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
                self.dirname = x['dirname']

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
            json.dump({'index':self._indexed_by_name,'files':self._files,'dirname':self.dirname},f)

        
    def __getitem__(self, key):
        return self._indexed_by_name[key]

    def get_fields(self, key, time_domain=None):
        """ 
        Return the fields corresponding to the key, and potentially a specific form of time averaging
        """
        if time_domain is not None:
            raise NotImplementedError
        file_keys = self[key]
        fields = cf.read([Path(self.dirname)/f for f in file_keys])
        fields = [f for f in fields if name_match(f, key)]
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
   





            


