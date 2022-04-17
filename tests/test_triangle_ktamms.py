import unittest
from unittest.case import _AssertRaisesContext
from triangle_ktamms import triangleArea

class test_formula(unittest.TestCase):

    def test_output(self):
        triangleArea.areaOfTriangle(1, 2) == 1;
        triangleArea.areaOfTriangle(72, 53) == 1908;
    
    def test_negativeInputs(self):
        with self.assertRaises(Exception):
            triangleArea.areaOfTriangle(-3, 2)

if __name__ == '__main__':
    unittest.main()