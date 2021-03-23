# 抽象工厂模式

# 在什么情况下应当使用抽象工厂模式:
# 1.一个系统不应当依赖于产品类实例如何被创建、组合和表达的细节，这对于所有形态的工厂模式都是重要的。
# 2.这个系统的产品有多于一个的产品族，而系统只消费其中某一族的产品。
# 3.同属于同一个产品族的产品是在一起使用的，这一约束必须在系统的设计中体现出来。（比如：Intel主板必须使用Intel CPU、Intel芯片组）
# 4.系统提供一个产品类的库，所有的产品以同样的接口出现，从而使客户端不依赖于实现。

# 抽象工厂模式的优点:
# 1. 分离接口和实现: 客户端使用抽象工厂来创建需要的对象，而客户端根本就不知道具体的实现是谁，客户端只是面向产品的接口编程而已。
#    也就是说，客户端从具体的产品实现中解耦。
# 2. 使切换产品族变得容易: 因为一个具体的工厂实现代表的是一个产品族，比如上面例子的从Intel系列到AMD系列只需要切换一下具体工厂。

# 抽象工厂模式的缺点:
# 不太容易扩展新的产品: 如果需要给整个产品族添加一个新的产品，那么就需要修改抽象工厂，这样就会导致修改所有的工厂实现类。

from abc import abstractmethod


class AbstractCpu:

    def __init__(self, series):
        self.series_name = series


class IntelCpu(AbstractCpu):
    pass


class AmdCpu(AbstractCpu):
    pass


class AbstractMainBoard:

    def __init__(self, series):
        self.series_name = series


class IntelMainBoard(AbstractMainBoard):
    pass


class AmdMainBoard(AbstractMainBoard):
    pass


class AbstractFactory:
    computer_name = ''

    @abstractmethod
    def create_cpu(self):
        pass

    @abstractmethod
    def create_main_board(self):
        pass


class IntelFactory(AbstractFactory):
    computer_name = 'Intel I7-series computer'

    def create_cpu(self):
        return IntelCpu('I7-6500')

    def create_main_board(self):
        return IntelMainBoard('Intel-6000')


class AmdFactory(AbstractFactory):
    computer_name = 'AMD 4 computer'

    def create_cpu(self):
        return AmdCpu('amd444')

    def create_main_board(self):
        return AmdMainBoard('AMD-4000')


class ComputerEngineer:

    def __init__(self):
        self.cpu = None
        self.main_board = None

    def prepare_hard_wares(self, factory):
        self.cpu = factory.create_cpu()
        self.main_board = factory.create_main_board()

    def make_computer(self, factory):
        self.prepare_hard_wares(factory)
        print(
            f"computer: {factory.computer_name}\n"
            f"cpu: {self.cpu.series_name}\n"
            f"mainboard:{self.main_board.series_name}\n"
        )


if __name__ == '__main__':
    engineer = ComputerEngineer()

    intel_factory = IntelFactory()
    engineer.make_computer(intel_factory)

    amd_factory = AmdFactory()
    engineer.make_computer(amd_factory)
