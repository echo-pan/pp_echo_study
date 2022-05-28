"""
4.士兵开枪
    需求：
    1）.士兵瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是扳机)
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量
分析：
    创建类：-士兵
            属性：名字、配枪
            方法：
                -开火：调用配枪的射击方法
    创建类：-枪
            属性：名字、子弹数、剩余子弹数
            方法：
                -发射子弹：
                    判断要发射的子弹数是否大于枪的剩余子弹数：
                        如果小于等于：用剩余子弹数减去发射的子弹数，并返回剩余子弹数
                        如果大于：打印-“子弹数不足，无法发射”
                -装子弹：
                    计算当前可装填子弹数=枪的子弹数-剩余子弹数
                    判断要装填子弹数是否大于可装填子弹数：
                        如果小于等于：把装填子弹数加到剩余子弹数里
                        如果大于：打印-“弹道空间不足，无法装填”

"""


# 创建类：-士兵
class Soldier():
    # 属性：名字、配枪
    def __init__(self, name, Gun):
        self.name = name
        self.withGun = Gun

    # 方法：
    # -开火：调用配枪的射击方法
    def fire(self, number):
        self.withGun.shoot(number)


# 创建类：-枪
class Gun():
    # 属性：名字、子弹数、剩余子弹数
    def __init__(self, name, bullet):
        self.name = name
        self.allBullet = bullet
        self.remainBullet = self.allBullet

    # 方法：
    # -发射子弹：
    def shoot(self, number):
        # 判断要发射的子弹数是否大于枪的剩余子弹数：
        # 如果小于等于：用剩余子弹数减去发射的子弹数，并返回剩余子弹数
        # 如果大于：打印 -“子弹数不足，无法发射”
        if number <= self.remainBullet:
            self.remainBullet -= number
        else:
            print("子弹数不足，无法发射")

    # -装子弹：
    def fill(self, number):
        # 计算当前可装填子弹数 = 枪的子弹数 - 剩余子弹数
        # 判断要装填子弹数是否大于可装填子弹数：
        # 如果小于等于：把装填子弹数加到剩余子弹数里
        # 如果大于：打印 -“弹道空间不足，无法装填”
        self.fillBullet = self.allBullet - self.remainBullet
        if number <= self.fillBullet:
            self.remainBullet += number
        else:
            print("弹道空间不足，无法装填")


if __name__ == '__main__':
    gun01 = Gun("AK47", 32)
    soldier01 = Soldier("瑞恩", gun01)
    soldier01.fire(32)
    print(gun01.remainBullet)
    gun01.fill(32)
    print(gun01.remainBullet)
