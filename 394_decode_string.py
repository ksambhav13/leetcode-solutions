# [394. Decode String](https://leetcode.com/problems/decode-string/)


class Solution:
    def decodeString(self, s: str) -> str:
        n_stack = []
        for ch in s:
            if ch == "]":
                w = ""
                while n_stack and n_stack[-1] != "[":
                    w = n_stack.pop() + w
                n_stack.pop()
                num = 0
                mul = 1
                while n_stack and n_stack[-1].isdigit():
                    num = mul * int(n_stack.pop()) + num
                    mul *= 10

                n_stack.append(w * num)
            else:
                n_stack.append(ch)

        return "".join(n_stack)


testcases = [
    "3[a]2[bc]",
    "3[a2[c]]",
    "2[abc]3[cd]ef",
    "3[z]2[2[y]pq4[2[jk]e1[f]]]ef",
]


for testcase in testcases:
    print(Solution().decodeString(testcase))
