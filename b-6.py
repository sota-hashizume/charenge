"""
    line one
    line two
    line three
"""
author = "sota hashizume"
author[0]
author[2]
author[3]
author[4]
author[5]
author[6]
author[7]
author[8]

author[-5]

"cat" + "in" + "hat"
"cat" + " in" + " the" + " hat"

"Sawyer" * 3

"We hold these truths...".upper()

"SO IT GOES.".lower()

"four score and...".capitalize()

"こんにちは、{}".format('ウィリアムフォークナー')

name = "ウィリアム・フォークナー"
"こんにちは、{}".format(name)

author = "ウィリアム・フォークナー"
year_born = "1897"

"{}は{}年に生まれました".format(author, year_born)

what = input("何が:")
when = input("いつ:")
where = input("どこで:")
do = input("何をした:")

r = "{}は{}に{}で{}。".format(what, when, where, do)
print(r)

"昨日はいい日だった。またあのような日が来るのを待ち望んでいる。".split("。")

first_three = "abc"
"+".join(first_three)

sentence = ["I", "bought", "a", "big", "bag", "."]
sen = "".join(sentence)
print(sen)
real_sen = " ".join(sentence)
print(real_sen)

s = "      The     "
s.strip(" ")
print(s)

equ = "The apple's products are very useful."
equ = equ.replace("a", "@")
print(equ)

try_2 = "This is a pen which i wanted"
try_2 = try_2.replace("i", "ｉ")
print(try_2)

"animal".index("m")

try:
    "animal".index("z")
except:
    print("Not found.")

"Cat" in "Cat in the hat."
"Bat" in "Cat in the hat."
"Potter" not in "Harry"

"彼女は\"そうだね\"と言った"
"彼女は'そうだね'と言った"
'彼女は"そうだね"と言った'

print("line1\nline2\nline3")

fict = ["こんにちは", "こんばんは", "おはようございます", "いただきます", "ご馳走様でした"]
fict[0:3]

ivan = "今日の3時に駅近のレストランで集合しましょう"
ivan[0:6]
ivan[6:22]

ivan[:6]
ivan[6:]
ivan[:]

p6 = "Camuu"
print(p6[0])
print(p6[1])
print(p6[2])
print(p6[3])
print(p6[4])

answer1 = "手紙"
answer2 = "両親"

p6_2 = "私は{}を書いて、{}に送った。".format(answer1, answer2)
print(p6_2)

p6_3 = "aldous Huxley was born in 1894. he was such a good guy.".title()
print(p6_3)

a = {"どこで": "遊園地で",
     "誰が": "妹が",
     "いつ": "昨日"}
print("今週末の日記：" + a["いつ"] + a["誰が"] + a["どこで"] + "楽しそうにしていた。")

b = "Where? When? Who?".split("?")
print(b)

fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0:-2] + "."
print(fox)

c = "A screaming comes across the sky.".replace("s", "$")
print(c)

"Hermingway".index("m")

d = "彼はいった\"なぜリンゴは木から落ちるのか\"と"
print(d)

print("three " + "three " + "three")
e = "three " * 3
e = e[0:-1]
print(e)

f = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
f_1 = f[:10]
print(f_1)

