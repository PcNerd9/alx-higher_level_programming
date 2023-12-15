from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)
    @property
    def size(self):
        return (self.width)
    
    @size.setter
    def size(self, value):
        self.size_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if (len(args) > 0):
            if (len(args) > 0):
                self.size_validator("width", args[0])
                self.id = args[0]
            if (len(args) > 1):
                self.size_validator("width", args[1])
                self.width = args[1]
                self.height = args[1]
            if (len(args) > 2):
                self.size_validator("width", args[2])
                self.x = args[2]
            if (len(args) > 3):
                self.size_validator("width", args[3])
                self.y = args[3]
        elif (len(kwargs) > 0):
            if ("id" in kwargs):
                self.size_validator("width", kwargs["id"])
                self.id = kwargs["id"]
            if ("size" in kwargs):
                self.size_validator("width", kwargs["size"])
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if ("x" in kwargs):
                self.size_validator("width", kwargs["x"])
                self.x = kwargs["x"]
            if ("y" in kwargs):
                self.size_validator("width", kwargs["y"])
                self.y = kwargs["y"]

    def to_dictionary(self):
        dictionary = {"id": self.id,
                      "x": self.x,
                      "size": self.width,
                      "y": self.y,
                      }
        return dictionary
