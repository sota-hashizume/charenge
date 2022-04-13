import re

l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)

print(matches)

import re

l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)

import re

zen = """Althoufh never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

import re

string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

import re

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)

import re
t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)


import re
text = """キリンは大昔から　__複数名詞__　の興味の対象でした。キリンは　__複数名詞__　の中で
        一番背が高いですが、科学者たちはそのような長い　__体の一部__　をどうやって獲得したのか説明できません。
        キリンの身長は　__数値__　__単位__　近くあり、その高さのほとんどは脚と　__体の一部__　によるものです。
       """
def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語(=ヒント)の部分は後を二つのアンダースコアで挟んでください。
    ヒントの単語にはアンダースコアを含めないでください。 __hint_hint__はダメです。　__hint__　はOKです。
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)


import re

line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)


import re

match = re.findall(".oo", "The ghost that says boo haunts the loo.")
print(match)

