# [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)


class Solution:
    def myAtoi(self, s: str) -> int:
        def round(num):
            max_num = 2147483648
            if num >= max_num:
                return max_num - 1
            elif num < -1 * max_num:
                return -1 * max_num
            else:
                return num

        number = None
        sign = None
        for ch in s:
            if (number is None) and (sign is None):
                if ch == " ":
                    continue
                elif ch in "+-":
                    sign = -1 if ch == "-" else 1
                    continue
            if ch.isdigit():
                number = 10 * (number or 0) + int(ch)
            else:
                break
        return round((sign or 1) * (number or 0))


testcases = [
    "42",
    "   -042",
    "1337c0d3",
    "0-1",
    "words and 987",
    "-91283472332",
    "+1",
    "+-12",
]


for testcase in testcases:
    print(Solution().myAtoi(testcase))
