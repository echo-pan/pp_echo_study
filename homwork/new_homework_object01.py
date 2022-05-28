"""
1、打印小猫爱吃鱼，小猫要喝水
	定义猫类
	   属性：name
	   方法：吃鱼、喝水
"""


class Cat():
    
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}爱吃鱼")

    def drink(self):
        print(f"{self.name}要喝水")


if __name__ == '__main__':
    cat = Cat("小猫")
    cat.eat()
    cat.drink()
    
