import subprocess as sp
from pathlib import Path as pas

# sp.call('echo "Hello"', shell=True)

#def __init__(self,hoge):
"""
name = input("名前を入力してください\n")
if(name):
    for counta in range(5):
        print(name + "＞連続攻撃！")
    print("対象の消滅を確認")
else:
    
        print("入力してください")
"""


Q1 = input ("おやつ300円以上買える Y／N\n")
if(Q1 != "Y"):
    print("ドーナツを買う")
Q2 = input ("甘いものがいい Y／N \n")
Q3 = input ("カロリーを気にしてる Y／N \n")
if (Q2 != "Y" and Q3 != "Y"):
    print("ポテチを買う")
elif(Q2 != "Y" and Q3 == "Y"):
    print("チーズタルトを買う")
else:
    print("ライ麦ケーキを買う")




"""
code = '1010018976'
print("code")
print(code[:3])
print(code[3:])
print(code[:3]+"-"+code[3:])

"""

"""
magic = "{0}は「{1}」の呪文を唱えた！{0}のHPが{2}回復した{3}"
hoge = magic.format('スライム','ホイミ',5,'!!!')
print (hoge)
"""
"""
chara = "かか力か"
i = "力" not in chara
print(i)
code = "123456789"
j = "7" in code
print(j)
"""
