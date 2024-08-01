class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class MyQueue:

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
            self.tail.next=newNode
            self.tail=newNode
        self.size+=1

            

    def pop(self) -> int:
        trav=self.head
        self.head=self.head.next
        self.size-=1
        data=trav.data
        del trav
        return data

        

    def peek(self) -> int:
        return self.head.data



    def empty(self) -> bool:
        return self.size==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()