class MinStack:

    def __init__(self):
        self.ms = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.ms and self.ms[-1] < val:
            return
        self.ms.append(val)

    def pop(self) -> None:
        val =self.stack.pop()
        if val == self.ms[-1]:
            self.ms.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ms[-1]