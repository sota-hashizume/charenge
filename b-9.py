import os
from tkinter import W
os.path.join("Users", "bob", "st.txt")

st = open("st.txt", "w")
st.write("Hi from Python!")
st.close()

st = open("st.txt", "w", encoding="utf-8")
st.write("Pythonからこんにちは")
st.close

with open("st.txt", "w") as f:
    f.write("Hi from Python!")

with open("st.txt", "r") as f:
    print(f.read())

my_list = []
with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)

import csv
with open("st.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

import csv
with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

# チャレンジ
with open("st.txt", "r") as f:
    print(f.read())

with open("st.txt", "w", encoding="utf-8") as f:
    f.write("好きな食べ物は何ですか？")

list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
import csv
with open("movie.csv", "w") as f:
    w = csv.writer(f, delimiter=",")      #これじゃだめです　　for構文使わないと
    w.writerow(list[0])
    w.writerow(list[1])
    w.writerow(list[2])

list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
import csv
with open("movies.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for movies_list in list:
        w.writerow(movies_list)

with open("movies.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for movies_list in list:


def hangman(word):
    wrong = 0
    stages = ["",
              "_____        ",
              "|            ",
              "|    |       ",
              "|    0       ",
              "|   /|\      ",
              "|   / \      ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

while wrong < len(stages) - 1:
    print("/n")
    msg = "１文字を予想してね"
    char = input(msg)
    if char in rletters:
        cind = rletters.index(char)
        board[cind] = char
        rletters[cind] = '$'
    else:
        wrong += 1
    print(" ".join(board))
    e = wrong + 1
    print("/n".join(stages[0:e]))
    if "_" not in board:
        print("あなたの勝ち！")
        print(" ".join(board))
        win = True
        break

if not win:
    print("/n".join(stages[0:wrong+1]))
    print("あなたの負け！正解は {}."format(word))


