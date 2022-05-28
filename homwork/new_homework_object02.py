"""
2、小明爱跑步，爱吃东西。
    1）小明体重75.0公斤
    2）每次跑步会减肥0.5公斤
    3）每次吃东西体重会增加1公斤
    4）小美的体重是45.0公斤

分析：
    创建类 -人类
        属性：名字、体重
        方法：-吃：吃一次东西，体重增加1kg
            -跑步：跑步一次，体重减少0.5kg
"""


class Human():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        self.weight += 1

    def run(self):
        self.weight -= 0.5


if __name__ == '__main__':
    human01 = Human("小明", 75)
    human02 = Human("小美", 45)
    human01.run()
    human02.eat()
    print(f"小明跑步后的体重是{human01.weight}kg,小美吃东西后的体重是{human02.weight}kg")
