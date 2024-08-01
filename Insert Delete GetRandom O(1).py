class RandomizedSet:

    def __init__(self):
        self.list=[]
        self.dict={}

        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.list.append(val)
        return True
        # self.dict{val}
        
        

    def remove(self, val: int) -> bool:
        # if val not in self.dict:
        #     return False
        # ele = self.list[-1]
        # rem = self.dict[val]
        # self.list[rem] = ele
        # self.dict[ele] = rem
        # self.list.pop()
        # del self.dict[val]
        # return True
        if val in self.list:
            return False
        else:
            self.list.remove(val)
            return True
        

        
        
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()