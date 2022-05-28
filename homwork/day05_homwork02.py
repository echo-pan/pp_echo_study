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
    分析：创建类 家具：属性 --> name，占地面积
        创建类 房子：属性 --> name，总面积，存放家具列表
                   方法 --> 放家具
"""


class Function:

    def __init__(self, name, f_area):
        self.name = name
        self.f_area = f_area


class House:

    def __init__(self, name, h_area):
        self.name = name
        self.h_area = h_area
        self.m_area = h_area
        self.function = []

    def fill_function(self, function):
        self.m_area = self.h_area - function.f_area
        self.function.append(function.name)

    def __str__(self):
        return f"该房子的户型是{self.name},总面积{self.h_area}平，家里放的家具有{self.function},家里剩余面积是{self.m_area}平"


if __name__ == '__main__':
    function01 = Function("床", 4)
    function02 = Function("桌子", 3)
    function03 = Function("椅子", 1.5)
    house01 = House("大三居室", 130)
    house01.fill_function(function01)
    print(house01)
