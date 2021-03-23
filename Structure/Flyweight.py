# 享元模式

# 意图：
# 运用共享技术有效地支持大量细粒度的对象

# 适用性：
# 一个应用程序使用了大量的对象。
# 完全由于使用大量的对象，造成很大的存储开销。
# 对象的大多数状态都可变为外部状态。
# 如果删除对象的外部状态，那么可以用相对较少的共享对象取代很多组对象。
# 应用程序不依赖于对象标识。由于Flyweight 对象可以被共享，对于概念上明显有别的对象，标识测试将返回真值

from abc import abstractmethod


class FlyweightBase:
    _instances = dict()  # 皴法实例化的对象内存地址

    @abstractmethod
    def __init__(self, *args, **kwargs):
        # 继承的子类必须初始化
        pass

    def __new__(cls, *args, **kwargs):
        print(cls._instances, type(cls))  # cls 就是你要实例化的子类如：obj = Spam(1,abc)
        return cls._instances.setdefault(
            (cls, args, tuple(kwargs.items())),  # key   （实例和参数）obj = Spam(y,x)
            super().__new__(cls)  # value  #实例化新的对象的内存地址
            # 调用自身的_instances字典，如果没有往父类找_instances字典
            # setdefault：判断_instances字典是否有该key:obj = Spam(y,x)实例 ,
            #               如果有，返回该key的value（上次实例化对象（内存地址））
            # setdefault： 如果找不到key：obj = Spam(y,x)实例 ，就在_instances字典就创建该key，value为新实例化对象（内存地址）
            #               返回该新创建key的value(该次实例化的对象（内存地址）
            # 这也就说明你实例化对象的时候，如果形参相同的话，不用实例化，直接返回已存在的实例的内存）
        )


class Spam(FlyweightBase):
    """精子类"""

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def test_data(self):
        print("精子准备好了", self.a, self.b)


class Egg(FlyweightBase):
    """卵类"""

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def test_data(self):
        print("卵子准备好了", self.x, self.y)


spam1 = Spam(1, 'abc')
spam2 = Spam(1, 'abc')
spam3 = Spam(3, 'DEF')

egg1 = Egg(1, 'abc')
print(id(spam1), id(spam2), id(spam3))