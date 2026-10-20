class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        stack = [-1]
        longest_val_substr = 0
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    longest_val_substr = max(i-stack[-1], longest_val_substr)
        return longest_val_substr
