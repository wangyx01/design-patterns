# 职责链模式

# 意图：
# 使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

# 适用性：
# 有多个的对象可以处理一个请求，哪个对象处理该请求运行时刻自动确定
# 你想在不明确指定接收者的情况下，向多个对象中的一个提交一个请求
# 可处理一个请求的对象集合应被动态指定


# 职责链模式（Chain of Responsibility）：使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。
# 适用场景：
# 1、有多个的对象可以处理一个请求，哪个对象处理该请求运行时刻自动确定；
# 2、在不明确指定接收者的情况下，向多个对象中的一个提交一个请求；
# 3、处理一个请求的对象集合应被动态指定。


class BaseHandler:
    '''处理基类'''

    def __init__(self, name):
        self.name = name
        self._successor = self

    def handle(self, request):
        pass

    # next_handler
    def successor(self, successor):
        # 与下一个责任者关联
        self._successor = successor


class RequestHandlerL1(BaseHandler):
    '''第一级请求处理者'''

    def __init__(self, name="TeamLeader"):
        super().__init__(name)

    def handle(self, request):
        if request < 500:
            print(f"审批者[{self.name}],请求金额[{request}],审批结果[审批通过]")
        else:
            print(f"\033[31;1m[{self.name}]无权审批,交给下一个审批者\033[0m")
            self._successor.handle(request)


class RequestHandlerL2(BaseHandler):
    '''第二级请求处理者'''

    def __init__(self, name="DeptManager"):
        super().__init__(name)

    def handle(self, request):
        if request < 5000:
            print("审批者[%s],请求金额[%s],审批结果[审批通过]" % (self.name, request))
        else:
            print("\033[31;1m[%s]无权审批,交给下一个审批者\033[0m" % self.name)
            self._successor.handle(request)


class RequestHandlerL3(BaseHandler):
    '''第三级请求处理者'''

    def __init__(self, name="CEO"):
        super().__init__(name)

    def handle(self, request):
        if request < 10000:
            print("审批者[%s],请求金额[%s],审批结果[审批通过]" % (self.name, request))
        else:
            print("\033[31;1m[%s]要太多钱了,不批\033[0m" % self.name)


class RequestAPI:
    h1 = RequestHandlerL1()
    h2 = RequestHandlerL2()
    h3 = RequestHandlerL3()

    h1.successor(h2)
    h2.successor(h3)

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def handle(self):
        '''统一请求接口'''
        self.h1.handle(self.amount)


if __name__ == "__main__":
    r1 = RequestAPI("Burgess", 10000)
    r1.handle()
    print(r1.__dict__)
