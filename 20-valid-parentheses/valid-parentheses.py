class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for bkt in s:
            if bkt in "([{":
                stack.append(bkt)
            else:
                #check if stack is empty
                if not stack:
                    return False

                if bkt == ")" and stack[-1] == "(":
                    stack.pop()
                elif bkt == "]" and stack[-1] == "[":
                    stack.pop()
                elif bkt == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
