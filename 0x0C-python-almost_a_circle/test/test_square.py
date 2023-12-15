import sys
sys.path.append("/home/pcnerd/All_My_Alx_projects/alx-higher_level_programming/0x0C-python-almost_a_circle/models")
import unittest
from square import Square

class TestSquareClass(unittest.TestCase):
    def test_square(self):
        square1 = Square(4, 3, 4, 10)
        self.assertEqual(square1.size, 4)
        self.assertEqual(square1.x, 3)
        self.assertEqual(square1.y, 4)
        self.assertEqual(square1.id, 10)
        square1.size = 20
        square1.height = 25
        square1.x = 5
        square1.y = 7
        square1.id = 0
        self.assertEqual(square1.width, 20)
        self.assertEqual(square1.height, 25)
        self.assertEqual(square1.x, 5)
        self.assertEqual(square1.y, 7)
        self.assertEqual(square1.id, 0)

    def test_square_type_init(self):
        with self.assertRaises(TypeError):
          Square("1", 3, 4, 10)
        with self.assertRaises(TypeError):
            Square(1, "2", 4, 10)
        with self.assertRaises(TypeError):
            Square(2, 1, "3", 10)
        with self.assertRaises(TypeError):
            Square(4, 2, "6", 30)

    def test_square_value_init(self):
        with self.assertRaises(ValueError):
            Square(0, 4, 3, 4)
        with self.assertRaises(ValueError):
            Square(1, -1, 4, 5)
        with self.assertRaises(ValueError):
            Square(2, -1, 5, 0)
        with self.assertRaises(ValueError):
            Square(6, 4, -2, 30)

    def test_square_area(self):
        square4 = Square(6, 5, 2, 5)
        self.assertEqual(square4.area(), 36)
        square4.size = 7
        self.assertEqual(square4.area(), 49)
        square4.size = 10
        self.assertEqual(square4.area(), 100)

    def test_square_str(self):
        square5 = Square(6, 3, 5, 7)
        self.assertEqual(str(square5), "[Square] (7) 3/5 - 6")
        square5.size = 4
        square5.x = 10
        square5.y = 0
        square5.id = 30
        self.assertEqual(str(square5), "[Square] (30) 10/0 - 4")

    def test_square_update(self):
        square7 = Square(4, 3, 2, 9)
        square7.update(1)
        self.assertEqual(square7.id, 1)
        square7.update(8, 4)
        self.assertEqual(square7.id, 8)
        self.assertEqual(square7.size, 4)
        self.assertEqual(str(square7), "[Square] (8) 3/2 - 4")
        square7.update(10, 12, 18)
        self.assertEqual(str(square7), "[Square] (10) 18/2 - 12")
        with self.assertRaises(ValueError):
            square7.update(10, 0, 2)
        square7.update(30, 4, 5, 8)
        self.assertEqual(str(square7), "[Square] (30) 5/8 - 4")
        square7.update(40, 3, 2, 5, 6, 7, 0, 32)
        self.assertEqual(str(square7), "[Square] (40) 2/5 - 3")

    def test_square_kwargs(self):
        square8 = Square(3, 4, 5, 7)
        square8.update(5, 8, 9, 10, 11)
        self.assertEqual(str(square8), "[Square] (5) 9/10 - 8")
        square8.update(id=6, size=5, x=1, y=1)
        self.assertEqual(str(square8), "[Square] (6) 1/1 - 5")
        square8.update(1, 2, 3, 4, 5, id=6, size=7, x=9, y=10)
        self.assertEqual(str(square8), "[Square] (1) 3/4 - 2")

    def test_square_to_dict(self):
        square9 = Square(5, 2, 5, 6)
        self.assertEqual(square9.to_dictionary(), {"id": 6, "x": 2, "size": 5, "y": 5})
        square9.update(6, 7, 2, 1, 10)
        self.assertEqual(square9.to_dictionary(), {"id": 6, "x":2, "size": 7, "y": 1})
        square9.update(id=10, size=30, x=40, y=50)
        self.assertEqual(square9.to_dictionary(), {"id": 10, "x": 40, "size": 30, "y": 50})


if __name__ == "__main__":
    unittest.main()
