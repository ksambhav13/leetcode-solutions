# [931. Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)
class FreqStack:
    def __init__(self):
        self.freq = {}
        self.freq_stack = []

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        if self.freq[val] - 1 >= len(self.freq_stack):
            self.freq_stack.append([val])
        else:
            self.freq_stack[self.freq[val] - 1].append(val)

    def pop(self) -> int:
        ret = self.freq_stack[-1].pop()
        if not self.freq_stack[-1]:
            self.freq_stack.pop()
        self.freq[ret] -= 1
        return ret


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
testcases = [
    [
        "FreqStack",
        "push",
        "push",
        "push",
        "push",
        "push",
        "push",
        "pop",
        "pop",
        "pop",
        "pop",
    ],
    [[], [5], [7], [5], [7], [4], [5], [], [], [], []],
    [
        "FreqStack",
        "push",
        "push",
        "push",
        "push",
        "pop",
        "pop",
        "push",
        "push",
        "push",
        "pop",
        "pop",
        "pop",
    ],
    [[], [1], [1], [1], [2], [], [], [2], [2], [1], [], [], []],
]

for i in range(0, len(testcases), 2):
    obj = globals()[testcases[i][0]](*testcases[i + 1][0])
    print(None)
    for j in range(1, len(testcases[i])):
        method = getattr(obj, testcases[i][j])
        print(method(*testcases[i + 1][j]))
