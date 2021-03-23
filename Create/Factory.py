# 工厂方法模式
# 这个和简单工厂有区别，简单工厂模式只有一个工厂，工厂方法模式对每一个产品都有相应的工厂
# 好处：增加一个运算类（例如N次方类），只需要增加运算类和相对应的工厂，两个类，不需要修改工厂类。
# 缺点：增加运算类，会修改客户端代码，工厂方法只是把简单工厂的内部逻辑判断移到了客户端进行
"""
工厂方法模式是简单工厂模式的衍生，解决了许多简单工厂模式的问题。
首先完全实现‘开－闭 原则’，实现了可扩展。其次更复杂的层次结构，可以应用于产品结果复杂的场合。 　　

工厂方法模式的对简单工厂模式进行了抽象。有一个抽象的Factory类（可以是抽象类和接口），这个类将不在负责具体的产品生产，而是只制定一些规范，
具体的生产工作由其子类去完成。在这个模式中，工厂类和产品类往往可以依次对应。
即一个抽象工厂对应一个抽象产品，一个具体工厂对应一个具体产品，这个具体的工厂就负责生产对应的产品。 　　

工厂方法模式(Factory Method pattern)是最典型的模板方法模式(Templete Method pattern)应用。
"""

from abc import abstractmethod


class ShapeFactory:

    def __init__(self, shape_name):
        self.shape_name = shape_name

    def get_shape(self):
        return self.shape_name


class Circle(ShapeFactory):

    def __init__(self):
        super().__init__("Circle")

    @staticmethod
    def draw():
        print("draw Circle")


class Rectangle(ShapeFactory):

    def __init__(self):
        super().__init__("Rectangle")

    @staticmethod
    def draw():
        print("draw Rectangle")


class ShapeInterfaceFactory:

    @abstractmethod
    def create(self):
        pass


class ShapeCircle(ShapeInterfaceFactory):
    def create(self):
        return Circle()


class ShapeRectangle(ShapeInterfaceFactory):
    def create(self):
        return Rectangle()


shape_interface = ShapeCircle()
obj = shape_interface.create()
obj.get_shape()
obj.draw()


shape_interface2 = ShapeRectangle()
obj2 = shape_interface2.create()
obj2.draw()
