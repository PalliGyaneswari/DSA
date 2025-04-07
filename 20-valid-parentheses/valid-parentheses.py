class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=='(':
                l.append(i)
            elif i=='{':
                l.append(i)
            elif i=='[':
                l.append(i)
            
            elif i == ')':
                if l and l[-1] == '(':  # Check if the last element is '('
                    l.pop()
                else:
                    return False
            elif i == '}':
                if l and l[-1] == '{':  # Check if the last element is '{'
                    l.pop()
                else:
                    return False
            elif i == ']':
                if l and l[-1] == '[':  # Check if the last element is '['
                    l.pop()
                else:
                    return False
        return not l 