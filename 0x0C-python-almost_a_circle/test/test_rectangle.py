import unittest
from unittest.mock import patch
import io
import sys
sys.path.append("/home/pcnerd/All_My_Alx_projects/alx-higher_level_programming/0x0C-python-almost_a_circle/models")
from rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    def test_rectangle(self):
        rectangle1 = Rectangle(4, 6, 3, 4, 10)
        self.assertEqual(rectangle1.width, 4)
        self.assertEqual(rectangle1.height, 6)
        self.assertEqual(rectangle1.x, 3)
        self.assertEqual(rectangle1.y, 4)
        self.assertEqual(rectangle1.id, 10)
        rectangle1.width = 20
        rectangle1.height = 25
        rectangle1.x = 5
        rectangle1.y = 7
        rectangle1.id = 0
        self.assertEqual(rectangle1.width, 20)
        self.assertEqual(rectangle1.height, 25)
        self.assertEqual(rectangle1.x, 5)
        self.assertEqual(rectangle1.y, 7)
        self.assertEqual(rectangle1.id, 0)

    def test_rectangle_type_init(self):
        with self.assertRaises(TypeError):
          Rectangle("1", 2, 3, 4, 10)
        with self.assertRaises(TypeError):
            Rectangle(1, "2", 3, 4, 10)
        with self.assertRaises(TypeError):
            Rectangle(2, 1, "3", 4, 10)
        with self.assertRaises(TypeError):
            Rectangle(4, 2, 2, "6", 30)

    def test_rectangle_value_init(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 4, 3, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, -1, 4, 5, 6)
        with self.assertRaises(ValueError):
            Rectangle(2, 4, -1, 5, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, 6, 4, -2, 30)

    def test_rectangle_type_set(self):
        rectangle2 = Rectangle(2, 3, 4, 5, 50)
        with self.assertRaises(TypeError):
            rectangle2.width = "2"
        with self.assertRaises(TypeError):
            rectangle2.height = "4"
        with self.assertRaises(TypeError):
            rectangle2.x = "3"
        with self.assertRaises(TypeError):
            rectangle2.y = "4"

    def test_rectangle_value_set(self):
        rectangle3 = Rectangle(4, 5, 5, 2, 1)
        with self.assertRaises(ValueError):
            rectangle3.width = 0
        with self.assertRaises(ValueError):
            rectangle3.height = 0
        with self.assertRaises(ValueError):
            rectangle3.x = -1
        with self.assertRaises(ValueError):
            rectangle3.y = -2

    def test_rectangle_area(self):
        rectangle4 = Rectangle(6, 3, 5, 2, 5)
        self.assertEqual(rectangle4.area(), 18)
        rectangle4.height = 7
        rectangle4.width = 7
        self.assertEqual(rectangle4.area(), 49)
        rectangle4.height = 10
        rectangle4.width = 4
        self.assertEqual(rectangle4.area(), 40)

    def test_rectangle_str(self):
        rectangle5 = Rectangle(6, 4, 3, 5, 7)
        self.assertEqual(str(rectangle5), "[Rectangle] (7) 3/5 - 6/4")
        rectangle5.width = 4
        rectangle5.height = 9
        rectangle5.x = 10
        rectangle5.y = 0
        rectangle5.id = 30
        self.assertEqual(str(rectangle5), "[Rectangle] (30) 10/0 - 4/9")

#    @patch('sys.stdout', new_callable=io.StringIO)
#   def test_rectangle_display(self, mock_stdout):
#        rectangle6 = Rectangle(6, 4, 3, 2, 5)
#        rectangle6.display()
#        printed_string = mock_stdout.getvalue().strip()

#        expected_string = '\n\n\n\n\n  ######\n  ######\n  ######\n  ######\n  ######'
#        self.assertMultiLineEqual(expected_string, printed_string)

    def test_rectangle_update(self):
        rectangle7 = Rectangle(4, 6, 3, 2, 9)
        rectangle7.update(1)
        self.assertEqual(rectangle7.id, 1)
        rectangle7.update(8, 4)
        self.assertEqual(rectangle7.id, 8)
        self.assertEqual(rectangle7.width, 4)
        self.assertEqual(str(rectangle7), "[Rectangle] (8) 3/2 - 4/6")
        rectangle7.update(10, 12, 18)
        self.assertEqual(str(rectangle7), "[Rectangle] (10) 3/2 - 12/18")
        with self.assertRaises(ValueError):
            rectangle7.update(10, 0, 2)
        rectangle7.update(30, 3, 4, 5, 8)
        self.assertEqual(str(rectangle7), "[Rectangle] (30) 5/8 - 3/4")
        rectangle7.update(40, 3, 2, 5, 6, 7, 0, 32)
        self.assertEqual(str(rectangle7), "[Rectangle] (40) 5/6 - 3/2")
    def test_rectagle_kwargs(self):
        rectangle8 = Rectangle(3, 4, 5, 6, 7)
        rectangle8.update(5, 8, 9, 10, 11)
        self.assertEqual(str(rectangle8), "[Rectangle] (5) 10/11 - 8/9")
        rectangle8.update(id=6, height=3, width=5, x=1, y=1)
        self.assertEqual(str(rectangle8), "[Rectangle] (6) 1/1 - 5/3")
        rectangle8.update(1, 2, 3, 4, 5, id=6, height=7, width=8, x=9, y=10)
        self.assertEqual(str(rectangle8), "[Rectangle] (1) 4/5 - 2/3")

    def test_rectangle_to_dict(self):
        rectangle9 = Rectangle(5, 3, 2, 5, 6)
        self.assertEqual(rectangle9.to_dictionary(), {"x": 2, "y": 5, "id": 6, "height": 3, "width": 5})
        rectangle9.update(6, 7, 2, 1, 10)
        self.assertEqual(rectangle9.to_dictionary(), {"x": 1, "y": 10, "id": 6, "height": 2, "width": 7})
        rectangle9.update(id=10, height=20, width=30, x=40, y=50)
        self.assertEqual(rectangle9.to_dictionary(), {"x": 40, "y": 50, "id": 10, "height": 20, "width": 30})

if __name__ == "__main__":
    unittest.main()
