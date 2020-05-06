# 自定义栈异常
class StackError(Exception):
    pass


class SStack:
    def __init__(self):
        # 约定列表的最后一个元素为栈顶
        self._elems = []

    def top(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems[-1]

    def is_empty(self):
        return self._elems == []

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems.pop()


if __name__ == "__main__":
    st = SStack()
    print(st.is_empty())
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
