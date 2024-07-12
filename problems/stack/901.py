# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.prices = []
        
    def next(self, price: int) -> int:
        if not self.prices:
            self.prices.append((price, 1))
            return 1
        
        if price < self.prices[-1][0]:
            self.prices.append((price, 1))
            return 1
        else:
            span = 1
            while self.prices and price >= self.prices[-1][0]:
                span += self.prices[-1][1]
                self.prices.pop()
            self.prices.append((price, span))
            return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)