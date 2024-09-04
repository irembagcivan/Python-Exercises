class Solution():
    def first_unique_character(self,s):
        char_count = {} # boş bir sözlük oluşturuldu

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        
        return -1

solution = Solution()
print(solution.first_unique_character("leetcode"))
print(solution.first_unique_character("loveleetcode"))
print(solution.first_unique_character("aabb"))

""" char_count = {
    'l': 2,
    'o': 2,
    'v': 1,
    'e': 4,
    't': 1,
    'c': 1,
    'd': 1
} """