"""
1、完成教程中未实现的作业:石头剪刀布
分析：
    比赛双方：我和系统比
    出拳方式：-我：通过input输入=保存成变量
            -系统：random方法随机出=保存成变量

    输赢判断：
        1、判断双方出拳是否一样
            如果一样：打印 平局
            如果不一样：继续判断
                2、列出赢的组合列表
                    如果[我，系统]在赢的列表，打印 你赢了
                    否则：你输了
2、正方形,三角形,九九乘法表
3.三角形的不同样子（右对齐，正三角形）
"""
import random


def game():
    user = input("请出拳：")
    machine = random.choice(["石头", "剪刀", "布"])
    win_list = [["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]
    print(f"系统出{machine}")
    if user == machine:
        print("平局")
    elif [user, machine] in win_list:
        print("你赢了")
    else:
        print("你输了")


def square():
    for m in range(4):
        print("* " * 4)
def tables():
    for line in range(1,10):
        for column in range(1,10):
            print(f"{line}*{column}="line * column,end="")

if __name__ == '__main__':
    tables()
