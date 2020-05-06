"""
链式队列
"""


# 队列异常
class QueueError(Exception):
    pass


# 队列结点
class Node(object):
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next


# 链式队列方法实现
class LQueue:
    def __init__(self):
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, elem):
        self.rear.next = Node(elem)
        self.rear = self.rear.next

    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")
        self.front = self.front.next
        return self.front.val

    def clear(self):
        self.front = self.rear


if __name__ == "__main__":
    lq = LQueue()
    print(lq.is_empty())

    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    while not lq.is_empty():
        print(lq.dequeue())
