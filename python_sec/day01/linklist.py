class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkList(object):
    def __init__(self):
        self.head = Node(None)

    def init_list(self, data):
        p = self.head
        for i in data:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next
        while p.next is not None:
            print(p.val, end="\t")
            p = p.next
        print()

    # 尾部插入新的节点
    def append(self, item):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(item)

    def get_length(self):
        n = 0
        p = self.head
        while p.next is not None:
            n += 1
            p = p.next
        return n

    def is_empty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head.next = None

    def get_item(self, index):
        p = self.head.next
        i = 0
        while i < index and p is not None:
            i += 1
            p = p.next
        if p is None:
            raise IndexError("list index out of range")
        else:
            return p.val

    def link_insert(self, index, item):
        if index < 0 or index >= self.get_length():
            raise IndexError("list index out of range")
        p = self.head
        i = 0
        while i < index:
            p = p.next
            i += 1
        node = Node(item)
        node.next = p.next
        p.next = node

    def delete(self, item):
        p = self.head
        while p.next is not None:
            if p.next.val == item:
                p.next = p.next.next
                break
            p = p.next
        else:
            raise ValueError("%d not in list"%(item))


if __name__ == "__main__":
    link = LinkList()
    l = [1, 2, 3, 4, 5]
    link.init_list(l)
    link.show()
    print(link.get_length())
    link.append(6)
    link.show()
