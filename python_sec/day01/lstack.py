# 自定义栈异常
class StackError(Exception):
    pass


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LStack:
    def __init__(self):
        # 标记栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, elem):
        self._top = Node(elem, self._top)
        # node.next = self._top
        # self._top = node

    def pop(self):
        if self._top is None:
            raise StackError("stack is empty")
        p = self._top
        self._top = p.next
        return p.val

    def top(self):
        if self._top is None:
            raise StackError("stack is empty")
        return self._top.val


if __name__ == "__main__":
    st = LStack()
    print(st.is_empty())
    st.push(10)
    st.push(20)
    st.push(30)
    print(st.top())
    while not st.is_empty():
        print(st.pop())

