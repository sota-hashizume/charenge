class Square:
    pass

print(Square)

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

my_rectangle = Rectangle(10, 20)
my_rectangle.print_size()

class Rectangle:
    recs = []
    def __init__(self, w, l) -> None:
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

#また色々消えました

from tkinter import W


class Rectangle:
    recs = []
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

class Lion:
    def __init__(self, name):
        self.name = name
    def __repr__(self) -> str:
        return self.name

lion = Lion("Dilbert")
print(lion)

class AlwaysPositive:
    def __init__(self, number) -> None:
        self.n = number
    def __add__(self, other):
        return abs(self.n  + other.n)

X = AlwaysPositive(-20)
Y = AlwaysPositive(10)
print(X + Y)

class Person:
    def __init__(self) -> None:
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

x = 10
if x is None:
    print("x はNone :(")
else:
    print("x はNoneじゃない")

x = None
if x is None:
    print("x はNone")
else:
    print("x はNoneじゃない :(")

#チャレンジ

class Square:
    square_list = []
    def __init__(self, w, l) -> None:
        self.width = w
        self.len = l
        self.square_list.append((self.width, self.len))

s1 = Square(10, 15)
s2 = Square(20, 40)
s3 = Square(15, 30)

print(Square.square_list)

class Square:
    square_list = []
    def __init__(self, e) -> None:
        self.edge = e
        self.square_list.append(self.edge)
    def print_size(self):
        print("{} by {} by {} by {}".format(self.edge, self.edge, self.edge, self.edge))

Square(10).print_size()
Square(39).print_size()

x = 10
if x is 10:
    print("xは10です。")
else:
    print("xは10じゃない")