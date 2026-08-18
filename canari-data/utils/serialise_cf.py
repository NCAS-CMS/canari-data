
import unittest
import cf
import numpy as  np

def serialise_data(o):
    units = str(o.Units)
    values = o.array.squeeze()
    shape = o.array.shape
    if not np.diff(values).any():
        # All the values are the same
        values = values[0:1]
    if len(values) == 1:
        values = values[0]
    values = values.tolist()
    return {'units': units, 'values': values, 'shape': shape}


def serialise(obj_type, object):
    methods = {
        "cfdata": serialise_data
    }
    if obj_type in methods:
        return methods[obj_type](object)
    else:
        return ValueError(f'Cannot serialise {obj_type}')

   
class TestSerialiser(unittest.TestCase):
     def test_cfdata(self): 
        x = cf.Data(np.array([1,2]))
        x.Units=cf.Units('K')
        y=serialise("cfdata",x)
        print(y)

if __name__=="__main__":
    unittest.main()
