class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


class MyStack:

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        

    def push(self, x: int) -> None:
        newNode=Node(x)
        if self.size==0:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.size+=1

        

    def pop(self) -> int:
        temp=self.head
        self.head=self.head.next
        data=temp.data
        del temp
        self.size-=1
        return data
        

    def top(self) -> int:
        return self.head.data
        

    def empty(self) -> bool:
        return self.size==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()