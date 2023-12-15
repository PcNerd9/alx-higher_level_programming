import unittest
import sys
sys.path.append("/home/pcnerd/All_My_Alx_projects/alx-higher_level_programming/0x0C-python-almost_a_circle/models")
from base import Base

class TestBaseClass(unittest.TestCase):
    def test_base(self):
        base1 = Base(10)
        self.assertEqual(base1.id, 10)
        base2 = Base()
        self.assertEqual(base2.id, 1)
        base3 = Base(20)
        self.assertEqual(base3.id, 20)
        base4 = Base()
        self.assertEqual(base4.id, 2)
        base5 = Base()
        base6 = Base()
        base7 = Base(40)
        base8 = Base()
        self.assertEqual(base8.id, 5)

if __name__ == "__main__":
    unittest.main()
