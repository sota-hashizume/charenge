from operator import index


name = "Ted"
for character in name:
    print(character)

coms = ("A.Development", "Friends", "Always Sunny")
for show in coms:
    print(show)

people = {"G. Bluth": "A. Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny"}
for show in people.values():
    print(show)

tv = ["gomes", "rodoriges", "chomes"]
i = 0
for change in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

tv = ["got", "narcos", "vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "friedns", "Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper
    all_shows.append(show)

for show in coms:
    show = show.upper
    all_shows.append(show)

print(all_shows)

for i in range(1, 11):
    print(i)

tv = []
for i in range(1, 11):
    tv.append(i)

print(tv)

x = 10
while x > 0:
    print("{}".format(x))  #ここさ、文字列にしたいからformat使ってるのよ。多分。。。。。
    x -= 1

print("Happy New Year!")

while True:
    print("Hellow, World!")

for i in range(0, 100):
    print(i)
    break

qs = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

for i in range(1, 4):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
    print(added)

while input('y or n?') != 'n':
    for i in range(1, 6):
        print(i)

list = ["ウォーキング", "アンドラージュ", "ザ・ソプラノ", "ヴァンパイア"]       #はい、だめです
n = 0
for i in list:
    print(list[n])
    n += 1

list = ["ウォーキング", "アンドラージュ", "ザ・ソプラノ", "ヴァンパイア"]  #理解できてない
for i in list:
    print(i)

for i in range(25, 51):
    print(i)


for index, show in enumerate(list):
    print(index)
    print(show)

correctAnswer = [3, 5, 15, 30]         #ごみ、禿げそう
while True:
    i = input("数字を入力してください：")
    print(i)
    if i == correctAnwer():
        print("正解!")
    elif i == "q":
        break
    else

list = [1, 3, 5, 15, 30]
while True:
    answer = input("Please type a number or \"q\" to quit:")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Type a number or \"q\" to quit")
    if answer in list:
        print("正解！")
    else:
        print("不正解！")

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
added = []
for i in list1:
    for j in list2:
        added.append(i * j)

print(added)