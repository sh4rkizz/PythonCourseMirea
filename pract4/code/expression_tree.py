from numpy import sum as np_sum
from numpy import prod as np_mlt


class Num:
    def __init__(self, n):
        self.number = n
        self.push_name = f'PUSH {n}'
        self.str_result = str(n)


class Operator:
    sign = ''
    operators = []
    push_list = []

    def __init__(self, *ops):
        self.operands = tuple(x.number for x in ops)
        self.name = self.__class__.__name__.upper()
        for x in ops:
            try:
                self.operators.append(x.name)
            except AttributeError:
                self.push_list.append(x.push_name)
        self.operators.insert(0, list(reversed(self.push_list)))
        self.str_result = f'({f" {self.sign} ".join(str(x.str_result) for x in ops)})'

    def get_it_right(self):
        self.operators.append(self.name)
        return self.operators


class Add(Operator):
    sign = '+'

    def __init__(self, *ops):
        super().__init__(*ops)
        self.number = np_sum(self.operands)


class Sub(Operator):
    sign = '-'

    def __init__(self, *ops):
        super().__init__(*ops)
        self.number = self.operands[0] - np_sum(self.operands[1:])


class Mul(Operator):
    sign = '*'

    def __init__(self, *ops):
        super().__init__(*ops)
        self.number = np_mlt(self.operands)


class Div(Operator):
    sign = '/'

    def __init__(self, *ops):
        super().__init__(*ops)
        self.number = float('{0:.4f}'.format(self.operands[0] / np_mlt(self.operands[1:])))


class PrintVisitor:
    @staticmethod
    def visit(result):
        return result.str_result


class CalcVisitor:
    @staticmethod
    def visit(result):
        return result.number


class StackVisitor:
    @staticmethod
    def get_code(result):
        res = result.get_it_right()
        out = '\n'.join(res[0])
        for x in res:
            try:
                out += '\n' + x
            except TypeError:
                pass
        return out


if __name__ == '__main__':
    ans = Div(Sub(Add(Num(7), Mul(Num(3), Num(2))), Num(5)), Num(4))
    print(PrintVisitor.visit(ans))
    print(CalcVisitor.visit(ans))
    print(StackVisitor.get_code(ans))
