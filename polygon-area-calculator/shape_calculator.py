class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h
    
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5
    
    def get_picture(self):
        if max(self.width, self.height) > 50:
            return 'Too big for picture.'
        else: 
            s=('*'*self.width + '\n')*self.height
            return s
    
    def get_amount_inside(self, shape):
        return (self.width//shape.width)*(self.height//shape.height)

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)





class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, s):
        self.width = s
        self.height = s
    
    def __str__(self):
        return 'Square(side={})'.format(self.width)
        
    def set_width(self, w):
        self.width = w
        self.height = w

    def set_height(self, h):
        self.width = h
        self.height = h


