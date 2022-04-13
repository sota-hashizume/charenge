pop =  []
jpop = []

def collect_songs():
    song = "曲名を入力してください"
    ask = "p か j のどちらかを入力してください。qで終わります: "
    while True:
        genre = input(ask)
        if genre == "q":
            break
        if genre == "p":
            p = input(song)
            pop.append(p)
        elif genre == "j":
            j = input(song)
            jpop.append(j)
        else:
            print("不正な値です。")
    print("pop songs: ", pop)
    print("jpop songs: ", jpop)

collect_songs()


class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

or1 = Orange(10, "dark orange")
print(or1)
or1.weight = 100
or1.color = "light orange"
or1.weight
print(or1.weight)
print(or1.color)

class Orange:
    def __init__(self, w, c):
        """weight（重さ）はグラム"""
        self.wight = w
        self.color = c
        self.mold = 0
        print("Created!")
    def rot(self, days, temp):
        """temp（温度）は摂氏"""
        self.mold = days * temp

orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def area(self):
        return self.width * self.length
    def change_size(self, w, l):
        self.width = w
        self.length = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())


#チャレンジ

class Apple:
    def __init__(self, c, w, r, s):
        self.color = c
        self.weight = w
        self.rediuce = r
        self.sweet = s
        print("Created!")

apple = Apple("red", 200, 5, 7)

import math
class Circle:
    def __init__(self, r):
        self.rediuce = r
    def area(self):
        return self.rediuce ** 2 * math.pi
        print("Created!")   # これが動作しないのは何でですか？

circle = Circle(3)
print(circle.area())

class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h
        print("Created!")
    def area(self):
        return self.bottom * self.height / 2

triangle = Triangle(15, 20)
print(triangle.area())

class Hexagon:
    def __init__(self, a, b, c, d, e, f):
        self.edge1 = a
        self.edge2 = b
        self.edge3 = c
        self.edge4 = d
        self.edge5 = e
        self.edge6 = f
        print("Created!")
    def calculate_parimeter(self):
        return self.edge1 + self.edge2 + self.edge3 + self.edge4 + self.edge5 + self.edge6

parimeter = Hexagon(2, 5, 3, 5, 7, 8)
print(parimeter.calculate_parimeter())