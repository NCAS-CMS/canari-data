import cf
from serialise_cf import serialise
import json
import unittest

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

class DomainSummary:
    """ 
    Holds a bounding box view of a domain, supplemented by cell_methods 
    See https://github.com/NCAS-CMS/cf-python/issues/482
    """
    def __init__(self, f):
        """ 
        Initialise with a field for which you wish to obtain the domain summary
        """
        # I am not sure about the coords and ancils, is that sufficient?
        coords = [a for a in f.coordinates().values() if a.dtype.kind not in "SU"]
        for a in coords:
            try:
                aa = a.get_bounds()
            except ValueError:
                if len(a.data) > 1:
                    a.set_bounds(a.create_bounds())
        self.bbox = [cf.Data.concatenate([a.lower_bounds.min(), a.upper_bounds.max()]) for a in coords]
        self.methods = get_cell_methods(f)
    def __str__(self):
        return self.json
    def __eq__(self, other):
        return str(other) == str(self)
    @property
    def json(self):
        return json.dumps({'bbox':[serialise('cfdata',b) for b in self.bbox], 'methods':self.methods})

class TestDomainSummary(unittest.TestCase):

    def test_bounded(self):
        """ Test domain summary works with well behaved bounded example"""
        f = cf.example_field(0)
        fds = DomainSummary(f)

    def test_unbounded(self):
        """ Test domain summary works with no bounds on a coordinate """
        f = cf.example_field(0)
        v1 = DomainSummary(f)
        x = f.coord('X')
        x.del_bounds()
        v2 = DomainSummary(f)
        self.assertEqual(v1,v2)

if __name__=="__main__":
    unittest.main()


