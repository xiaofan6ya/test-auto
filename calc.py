"""简单计算模块。divide 在除数为 0 时抛出带说明的 ValueError。"""


def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为 0：divide 的第二个参数 b 不允许为 0")
    return a / b


def add(a, b):
    return a + b
