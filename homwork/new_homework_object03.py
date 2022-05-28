"""
3、摆放家具
    需求：
    1）.房子有户型，总面积和家具名称列表
       新房子没有任何的家具
    2）.家具有名字和占地面积，其中
       床：占4平米
       衣柜：占2平面
       餐桌：占1.5平米
    3）.将以上三件家具添加到房子中
    4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

分析：
    创建类 -房子
            属性：户型、总面积、剩余面积、放的家具列表
            方法：
               -放家具：每放1件家具，就用剩余面积减去家具的面积，并把家具添加到家具列表
               -打印房子：打印房子的户型，总面积，剩余面积，家具名称列表
    创建类 -家具
            属性：名字、占地面积
"""


# 创建类 - 房子
class House():
    # 属性：户型、总面积、剩余面积、放的家具列表
    def __init__(self, houseType, totalArea):
        self.houseType = houseType
        self.totalArea = totalArea
        self.remainArea = self.totalArea
        self.allFurniture = []

    # 方法：
    # -放家具：每放1件家具，就用剩余面积减去家具的面积，并把家具添加到家具列表
    def furnished(self, Furniture):
        self.remainArea -= Furniture.area
        self.allFurniture.append(Furniture.name)
        # print(self.remainArea,self.allFurniture)

    # -打印房子：打印房子的户型，总面积，剩余面积，家具名称列表
    def des_house(self):
        print(f"这是一个{self.houseType},总面积是{self.totalArea},家里放了{self.allFurniture},剩余面积是{self.remainArea}")


# 创建类 - 家具
class Furniture():

    # 属性：名字、占地面积
    def __init__(self, name, area):
        self.name = name
        self.area = area


if __name__ == '__main__':
    house01 = House("三居室", 130)
    furniture01 = Furniture("床", 4)
    furniture02 = Furniture("衣柜", 2)
    furniture03 = Furniture("餐桌", 1.5)
    house01.furnished(furniture01)
    house01.furnished(furniture02)
    house01.furnished(furniture03)
    house01.des_house()
