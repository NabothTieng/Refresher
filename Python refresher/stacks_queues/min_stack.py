class MinStack:

    def __init__(self):
        self.ledger = []

    def push(self, val: int) -> None:
        self.ledger.append(val)

    def pop(self) -> None:
        if self.ledger:
            self.ledger.pop()

    def top(self) -> int:
        return self.ledger[-1]

    def getMin(self) -> int:
        return min(self.ledger)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()