class Rectangle:
    def __new__(cls, w, h):
        if w == h:
            result = Square.__new__(Square, w)
            result.__init__(w)
            return result
        else:
            return super().__new__(cls)

    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h
    
    def __repr__(self):
        return f"Rectangle(width={self.w}, height={self.h})"


class Square:
    def __new__(cls, side):
        return object.__new__(cls)

    def __init__(self, side):
        self.w = side
        self.h = side
    
    def __repr__(self):
        return f"Square(width={self.w}, height={self.h})"

    
r = Rectangle(5, 5)
print(r)