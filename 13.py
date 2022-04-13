from turtle import circle


class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)

type("Hello, world!")
type(200)
type(200.1)


#ポリモーフィズムなしの場合
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if isinstance(a_shape, Triangle):
        a_shape.draw_triangle()
    if isinstance(a_shape, Square):
        a_shape.draw_square()
    if isinstance(a_shape, Circle):
        a_shape.draw_circle()
#ポリモーリフィズムありの場合
shapes = [tr2, sq2, cr2]
for a_shape in shapes:
    a_shape.draw()


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def print_size(self):
        print("{} by {}".format(self.width, self.length))

my_shape = Shape(74, 189)
my_shape.print_size()

class Square(Shape):
    pass

a_square = Square(30, 20)
a_square.print_size()

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def print_size(self):
        print("{} by {}".format(self.width, self.length))

class Square(Shape):
    def area(self):
        return self.width * self.length

a_square = Square(20, 30)
print(a_square.area())



class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def print_size(self):
        print("{} by {}".format(self.width, self.length))

class Square(Shape):
    def area(self):
        return self.width * self.length
    def print_size(self):
        print("この四角形の幅は{},縦は{}です。".format(self.width, self.length))

a_square = Square(15, 21)
a_square.print_size()

class Child_square(Square):
    pass

child_square = Child_square(2.3, 1.7)
child_square.print_size()
print(child_square.area())


class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

sota = Person("Sota Hashizume")
jhon = Dog("Jhon", "German Shepherd", sota)
print(jhon.owner.name)
print(jhon.breed)

#チャレンジ


class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        return 2 * (self.width + self.len)

class Square:
    def __init__(self, e):
        self.edge = e
    def caluculate_perimeter(self):
        return 4 * self.edge

rectangle = Rectangle(5, 8)
square = Square(6)
print(rectangle.calculate_perimeter())
print(square.caluculate_perimeter())

class Square:
    def __init__(self, e):
        self.edge = e
    def calculate(self):
        return self.edge * 4
    def change_size(self, p, m):
        self.plus = p
        self.minus = m
        return self.edge + self.plus - self.minus

square = Square(8)
print(square.calculate())
change_size = square.change_size(2) #こいつだめ
print(square.calculate())
change_size = Square(square.change_size(2, 0))
print(change_size.calculate())
change_size = Square(square.change_size(0, 5))
print(change_size.calculate())

class Shape:
    def what_am_I(self):
        print("I am a {}.".format(self))

shape = Shape.what_am_I("circle")

class Shape:
    def what_am_I(self):
        print("My total length is {}cm.".format(self))

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        return 2 * (self.width + self.len)

class Square(Shape):
    def __init__(self, e):
        self.edge = e
    def caluculate_perimeter(self):
        return 4 * self.edge

rectangle = Rectangle(4, 5)
rectan = rectangle.calculate_perimeter()
rectan_len = Rectangle.what_am_I(rectan)

square = Square(7)
squa = square.caluculate_perimeter()
square_len = Square.what_am_I(squa)


class Horse:
    def __init__(self, name, rider):
        self.rider = rider
        self.name = name

class Rider:
    def __init__(self, name):
        self.name = name

sota = Rider("Sota Hashizume")
horse = Horse("Kokuen", sota)
print(horse.rider.name)