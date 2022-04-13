from random import random


"Hello".upper()
"Hello".replace("o", "@")

fruit = list()
fruit

fruit = ["Apple", "Orange", "Pear"]
fruit

fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")
fruit

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
random

fruit = ["Apple", "Orange", "Pear"]
fruit[0]
fruit[1]
fruit[2]

colors = ["blue", "green", "yellow"]
colors
colors[2] = "red"
colors

colors = ["blue", "green", "yellow"]
colors
item = colors.pop()
item
colors

colors = ["blue", "green", "yellow"]
"green" in colors

colors = ["blue", "green", "yellow"]
"black" not in colors

len(colors)

color1 = ["bule", "green", "yellow"]
color2 = ["orange", "pink", "black"]
color2 + color1

len(color1 + color2)

colors = ["puple", "blue", "green"]

guess = input("何色でしょう？（入力してください）:")

if guess in colors:
    print("大当たり！")
else:
    print("ハズレ。。")

my_tuple = tuple()
my_tuple

my_tuple = ("M.Jackson", 1985, True)
my_tuple

("self_taught",)

(9) + 1

dys = ("1985", "Brave New World", "Fahrenheit 451")
dys[1] = "Handmaid's Tale" #タプルは要素の追加、変更等はできませんよ
dys[2]

dys = ("1985", "Brave New World", "Fahrenheit 451")
"1985" in dys

fruits = {"Apple": "red",
          "Banana": "yellow"}
fruits
fruits["Orange"] = "orange"
del fruits["Banana"]

fruits

songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live"}

n = input("数字を入力してください:")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("見つかりません。")

list = []

rap = ["カニエウィストン", "ジェイz", "エミエム", "ナズ"]
rock = ["ポブディラン", "ザビートルズ", "レッドツェッペリン"]
djs = ["ゼッズデッド", "ティエスト"]

list.append(rap)
list.append(rock)
list.append(djs)

print(list)

rap = list[0]
print(rap)

rap = list[0]
rap.append("ケンドリックラマー")
print(rap)
print(list)

locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

eights = ["Edgar Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]

authors = (eights, nines)
print(authors)

bday = {"gfhao": "7.43.24.243",
        "hgaghao": "3.423.52.3"}

my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)

ny = {
    "座標": (40.234, 74.4323),
    "セレブ": [
        "ウッディアレン",
        "ジェイZ",
        "ケビンベーコン",
    ],
    "事実":{
        "州": "ニューヨーク",
        "国": "アメリカ",
    }
}

my_features = {"身長": "189",
               "好きな色": "green",
               "好きな作家": "東野圭吾",
               "好きなブランド": "tomorrowland"}

question = input("身長、好きな色、好きな作家、好きなブランド；これらの中から質問してください:")        #微妙いな
print(my_features[question])          #微妙いな

real_question = input("type a feature that you wanna know:")

if real_question in my_features:
    print(my_features[real_question])
else:
    print("the question couldn't be answered")
