class StockSpanner:

    def __init__(self):
        self.stack=[]


    def next(self, price: int) -> int:
        s=self.stack
        curprice=price
        curspan=1
        while s and s[len(s)-1][0]<=curprice:
            prevprice,prevspan=s.pop()
            curspan+=prevspan
        s.append((curprice,curspan))
        return curspan



        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)