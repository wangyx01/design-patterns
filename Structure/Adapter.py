# 适配器模式

# 意图：
# 将一个类的接口转换成客户希望的另外一个接口。Adapter 模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。

# 适用性：
# 你想使用一个已经存在的类，而它的接口不符合你的需求。
# 你想创建一个可以复用的类，该类可以与其他不相关的类或不可预见的类（即那些接口可能不一定兼容的类）协同工作。
# (仅适用于对象Adapter)你想使用一些已经存在的子类，但是不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。

# 应用场景：希望复用一些现存的类，但是接口又与复用环境要求不一致。


# 球员类
class Player:

    def __init__(self, name=''):
        self.name = name

    def attack(self):
        pass

    def defense(self):
        pass


# 中锋（目标类）
class Center(Player):

    def __init__(self, name):
        super().__init__(name)

    def attack(self):
        print(f"中锋{self.name} 进攻")

    def defense(self):
        print(f"中锋{self.name} 防守")


# 外籍中锋（待适配类）
# 中锋
class ForeignCenter(Player):

    def __init__(self, name):
        super().__init__(name)

    def foreign_attack(self):
        print(f"外籍中锋{self.name} 进攻")

    def foreign_defense(self):
        print(f"外籍中锋{self.name} 防守")


# 翻译(适配类)
class Translator(Player):

    def __init__(self, name):
        super().__init__(name)
        self.foreignCenter = ForeignCenter(name)

    def attack(self):
        self.foreignCenter.foreign_attack()

    def defense(self):
        self.foreignCenter.foreign_defense()


def client():
    c = Center('Test')
    c.attack()
    c.defense()
    m = Translator('麦克格雷迪')
    m.defense()
    m.attack()
    return


if __name__ == '__main__':
    client()
