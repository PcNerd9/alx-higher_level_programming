#!usr/bin/python3
from base import Base

class Rectangle(Base):
    def size_validator(self, val_name, value):
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(val_name))
        elif (value <= 0):
            raise ValueError("{} must be > 0".format(val_name))

    def position_validator(self, val_name, value):
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(val_name))
        elif (value < 0):
            raise ValueError("{} must be >= 0".format(val_name))

    def __init__(self, width, height, x=0, y=0, id=None):
        self.size_validator("width", width)
        self.size_validator("height", height)
        self.position_validator("x", x)
        self.position_validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.size_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.size_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        self.position_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        self.position_validator("y", value)
        self.__y = value

    def area(self):
        return (self.__height * self.__width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.y, self.__width, self.__height))

    def display(self):
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        if (len(args) > 0):
            if (len(args) >= 1):
                self.id = args[0]
            if (len(args) >= 2):
                self.size_validator("width", args[1])
                self.width = args[1]
            if (len(args) >= 3):
                self.size_validator("height", args[2])
                self.height = args[2]
            if (len(args) >= 4):
                self.position_validator("x", args[3])
                self.x = args[3]
            if (len(args) >= 5):
                self.position_validator("y", args[4])
                self.y = args[4]
        else:
            if ("id" in kwargs):
                self.id = kwargs["id"]
            if ("height" in kwargs):
                self.size_validator("height", kwargs["height"])
                self.__height = kwargs["height"]
            if ("width" in kwargs):
                self.size_validator("width", kwargs["width"])
                self.__width = kwargs["width"]
            if ("x" in kwargs):
                self.position_validator("x", kwargs["x"])
                self.__x = kwargs["x"]
            if ("y" in kwargs):
                self.position_validator("y", kwargs["y"])
                self.__y = kwargs["y"]

    def to_dictionary(self):
        dictionary = {"x": self.__x,
                      "y": self.__y,
                      "id": self.id,
                      "height": self.__height,
                      "width": self.__width
                      }
        return dictionary
