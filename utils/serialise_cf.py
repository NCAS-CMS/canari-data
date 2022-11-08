
import unittest
import cf
import numpy as  np

def serialise_data(o):
    units = str(o.Units)
    values = o.array.squeeze()
    shape = o.array.shape
    if len(values) == 1:
        values = float(values[0])
    else:
        values = values.tolist()
    return {'units': units, 'values': values, 'shape': shape}


def serialise(object):
    methods = {
        "<class 'cf.data.data.Data'>": serialise_data
    }
    otype = str(type(object))
    if otype in methods:
        return methods[otype](object)
    else:
        return ValueError(f'Cannot serialise {otype}')

   
class TestSerialiser(unittest.TestCase):
     def test_cfdata(self): 
        x = cf.Data(np.array([1,2]))
        x.Units=cf.Units('K')
        y=serialise(x)
        print(y)

if __name__=="__main__":
    unittest.main()
