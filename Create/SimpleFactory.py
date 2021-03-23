# 简单工厂模式
# 严格来说，简单工厂模式不是GoF总结出来的23种设计模式之一

# 意图：
# 定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类

# 适用性：
# 当一个类不知道它所必须创建的对象的类的时候
# 当一个类希望由它的子类来指定它所创建的对象的时候
# 当类将创建对象的职责委托给多个子类中的某一个

# 优点：客户端不需要修改代码
# 缺点：当需要增加新的运算类的时候，不仅需新加运算类，还要修改工厂类，违反了开闭原则


from abc import abstractmethod


class Shape:
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("draw Circle")


class Rectangle(Shape):
    def draw(self):
        print("draw Rectangle")


class ShapeFactory:

    @staticmethod
    def create(shape):
        if shape == "Circle":
            return Circle()
        if shape == "Rectangle":
            return Rectangle()
        return None


factory = ShapeFactory()
obj = factory.create("Circle")
obj.draw()
