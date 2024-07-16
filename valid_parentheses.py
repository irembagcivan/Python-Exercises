class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        
        matching = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        x = []
        
        for char in s:
            if char in matching:
                x.append(char)
            else:
                if not x or matching[x.pop()] != char:
                    return False
        
        return len(x) == 0

# Örnek kullanım
solution = Solution()
print(solution.isValid("()"))       
print(solution.isValid("(]"))       
print(solution.isValid("()[]{}"))   
