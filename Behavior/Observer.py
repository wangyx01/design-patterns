# 观察者模式

# 意图：
# 定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时, 所有依赖于它的对象都得到通知并被自动更新。

# 适用性：
# 当一个抽象模型有两个方面, 其中一个方面依赖于另一方面。将这二者封装在独立的对象中以使它们可以各自独立地改变和复用。
# 当对一个对象的改变需要同时改变其它对象, 而不知道具体有多少对象有待改变。
# 当一个对象必须通知其它对象，而它又不能假定其它对象是谁。换言之, 你不希望这些对象是紧密耦合的

# 观察者（Observer）模式又名发布-订阅（Publish/Subscribe）模式
# 当我们希望一个对象的状态发生变化，那么依赖与它的所有对象都能相应变化(获得通知),
# 那么就可以用到Observer模式， 其中的这些依赖对象就是观察者的对象，那个要发生变化的对象就是所谓’观察者’

class ObserverBase:
    '''观察者基类'''  # 放哨者

    def __init__(self, name):
        self._observerd_list = []  # 被通知对象
        self.name = name

    def attach(self, observe_subject):
        '''
        添加要观察的对象
        :param observe_subject:
        :return:
        '''
        if observe_subject not in self._observerd_list:
            self._observerd_list.append(observe_subject)
            print(f"[{self.name}]已经将[{observe_subject}]加入观察队列...")

    def detach(self, observe_subject):
        '''
        解除观察关系
        :param observe_subject:
        :return:
        '''
        try:
            self._observerd_list.remove(observe_subject)
            print(f"不再观察[{observe_subject}]")
        except ValueError:
            pass

    def notify(self):
        '''
        通知所有被观察者
        :return:
        '''
        for objserver in self._observerd_list:
            objserver.update(self)


class Observer(ObserverBase):
    '''观察者类'''

    def __init__(self, name):
        super().__init__(name)
        self._msg = ''

    @property  # 外部执行d.eat 去掉括号
    def msg(self):
        '''
        当前状况
        :return:
        '''
        return self._msg

    @msg.setter  # 设置属性（一个方法变成一个静态的属性）
    def msg(self, content):
        self._msg = content
        self.notify()


# 目前结论：一个方法变成一个静态的属性 （装饰了@property）
# 通过另外一个相同名字的方法（装饰@msg.setter ）进行修改该属性
# 简单： d = Observer('xxx')
# print(d.msg)  结果：空
# d.msg = 'xxx'
# #这种形式调用该对象有装饰setter的方法，xxx作为形参
# print(d.msg)  结果：xxx


class GCDViewer:
    '''
    共军被观察者
    '''

    def update(self, observer_subject):
        print(f"共军:收到[{observer_subject.name}]消息[{observer_subject.msg}] ")


class GMDViewer:
    '''
    国军被观察者
    '''

    def update(self, observer_subject):
        print(f"国军:收到[{observer_subject.name}]消息[{observer_subject.msg}] ")


if __name__ == "__main__":
    observer1 = Observer("共军放哨者")
    observer2 = Observer("国军放哨者")

    gongjun1 = GCDViewer()
    guojun1 = GMDViewer()

    observer1.attach(gongjun1)
    observer1.attach(guojun1)

    observer2.attach(guojun1)

    observer1.msg = "\033[32;1m敌人来了...\033[0m"

    observer2.msg = "\033[31;1m前方发现敌人,请紧急撤离,不要告诉共军\033[0m"
