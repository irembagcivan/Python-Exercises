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

# ilhanın çözümü

# while True:
#     metin = input("Metin giriniz: ")

#     deger1 = True
#     for i in range(0, len(metin)):
#         if metin[i] == '(':
#             if metin[i + 1] == ')':
#                 deger1 = True

#             else:
#                 deger1 = False

#     deger2 = True
#     for i in range(0, len(metin)):
#         if metin[i] == '[':
#             if metin[i + 1] == ']':
#                 deger2 = True

#             else:
#                 deger2 = False

#     deger3 = True
#     for i in range(0, len(metin)):
#         if metin[i] == '{':
#             if metin[i + 1] == '}':
#                 deger3 = True

#             else:
#                 deger3 = False

#     if deger1 == True and deger2 == True and deger3 == True:
#         print("True")

#     else:
#         print("False")
