# 创建者模式

# 意图：
# 将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示

# 适用性：
# 1. 当创建复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时。
# 2. 当构造过程必须允许被构造的对象有不同的表示时。

# 建造者模式
# 相关模式：思路和模板方法模式很像，模板方法是封装算法流程，对某些细节，提供接口由子类修改，建造者模式更为高层一点，将所有细节都交由子类实现。
# 建造者模式：将一个复杂对象的构建与他的表示分离，使得同样的构建过程可以创建不同的表示。

# 基本思想
# 某类产品的构建由很多复杂组件组成；
# 这些组件中的某些细节不同，构建出的产品表象会略有不同；
# 通过一个指挥者按照产品的创建步骤来一步步执行产品的创建；
# 当需要创建不同的产品时，只需要派生一个具体的建造者，重写相应的组件构建方法即可。

from abc import abstractmethod


# 建造者基类
class PersonBuilder:

    @abstractmethod
    def build_head(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


# 胖子
class PersonFatBuilder(PersonBuilder):
    type = "胖子"

    def build_head(self):
        print(f"构建{self.type}的大。。。。。头")

    def build_body(self):
        print(f"构建{self.type}的身体")

    def build_arm(self):
        print(f"构建{self.type}的手")

    def build_leg(self):
        print(f"构建{self.type}的脚")


# 瘦子
class PersonThinBuilder(PersonBuilder):
    type = "瘦子"

    def build_head(self):
        print(f"构建{self.type}的头")

    def build_body(self):
        print(f"构建{self.type}的身体")

    def build_arm(self):
        print(f"构建{self.type}的手")

    def build_leg(self):
        print(f"构建{self.type}的脚")


# 指挥者
class PersonDirector:

    def __init__(self, pd=None):
        self.pd = pd

    def create_pereson(self):
        self.pd.build_head()
        self.pd.build_body()
        self.pd.build_arm()
        self.pd.build_leg()


def client():
    pb = PersonThinBuilder()
    pd = PersonDirector(pb)
    pd.create_pereson()

    pb2 = PersonFatBuilder()
    pd.pd = pb2
    pd.create_pereson()
    return


if __name__ == '__main__':
    client()
