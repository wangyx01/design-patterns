# 解释器模式

# 意图：
# 给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子。

# 适用性：
# 当有一个语言需要解释执行,并且你可将该语言中的句子表示为一个抽象语法树时，可使用解释器模式。而当存在以下情况时该模式效果最好：
# 1. 该文法简单对于复杂的文法,文法的类层次变得庞大而无法管理。此时语法分析程序生成器这样的工具是更好的选择。
#    它们无需构建抽象语法树即可解释表达式,这样可以节省空间而且还可能节省时间。
# 2. 效率不是一个关键问题最高效的解释器通常不是通过直接解释语法分析树实现的,而是首先将它们转换成另一种形式。
#    例如，正则表达式通常被转换成状态机。但即使在这种情况下,转换器仍可用解释器模式实现,该模式仍是有用的。


from abc import abstractmethod


class Context:
    def __init__(self, input):
        self.input = input
        self.output = ""


class AbstractExpression:

    @abstractmethod
    def interpret(self, context):
        pass


class Expression(AbstractExpression):

    def interpret(self, context):
        print("terminal interpret")


class NonterminalExpression(AbstractExpression):

    def interpret(self, context):
        print("Nonterminal interpret")


if __name__ == "__main__":
    context = Context("input")
    c = [
        Expression(), NonterminalExpression(),
        Expression(), Expression()
    ]
    for a in c:
        a.interpret(context)
