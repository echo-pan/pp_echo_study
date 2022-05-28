"""
4.士兵开枪
    需求：
    1）.士兵瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是扳机)
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量
    需求分析：
        创建类 士兵：属性--> name，weapon
                方法：<装子弹>    <射击>
        创建类 枪：属性--> name
                方法：<装子弹>   <发射子弹>
"""


class Gun:

    def __init__(self, name):
        self.name = name
        self.bullet_number = 0
        self.biggest_number = 30

    def fill_bullet(self, fill_number):
        if fill_number > 0:
            for i in range(fill_number):
                if self.bullet_number < self.biggest_number:
                    self.bullet_number += 1
                else:
                    print("已经填满了")
                    break
            print(f"总共装填了{self.bullet_number}发子弹")
        else:
            print("装填子弹数量输入非法")

    def shot_bullet(self, shot_number):
        if shot_number > 0:
            count = 0
            for i in range(shot_number):
                if self.bullet_number > 0:
                    self.bullet_number -= 1
                    count += 1
                else:
                    print("已经没子弹了")
                    break
            print(f"总共发射了{count}发子弹")
        else:
            print("射击子弹数量输入非法")


class Solder:

    def __init__(self, name, weapon:Gun):
        self.name = name
        self.weapon = weapon

    def maintain_weapon(self, in_number):
        self.weapon.fill_bullet(in_number)

    def use_weapon(self, out_number):
        self.weapon.shot_bullet(out_number)

    def __str__(self):
        return f"士兵{self.name}有一把{self.weapon.name},剩余{self.weapon.bullet_number}发子弹"


if __name__ == '__main__':
    gun01 = Gun("ak47")
    # gun01.fill_bullet(30)
    # gun01.shot_bullet(31)
    solder01 = Solder("Ryan", gun01)
    solder01.maintain_weapon(22)
    solder01.use_weapon(2)
    print(solder01)