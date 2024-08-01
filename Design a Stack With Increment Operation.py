class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.size = 0
        self.head = None

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            newNode = Node(x)
            newNode.next = self.head
            self.head = newNode
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        temp = self.head
        self.head = self.head.next
        data = temp.data
        del temp
        self.size -= 1
        return data

    def increment(self, k: int, val: int) -> None:
        if self.size == 0:
            return
        current = self.head
        elements = []
        while current:
            elements.append(current)
            current = current.next
        limit = min(k, self.size)
        for i in range(limit):
            elements[-(i+1)].data += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k, val)
