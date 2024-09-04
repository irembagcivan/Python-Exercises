class Solution():
    def length_of_last_word(self,s):
        words = s.split(" ")

        if not words:
            return 0
        
        last_word = words[-1]

        return len(last_word)

        
solution = Solution()
print(solution.length_of_last_word("hello world"))
print(solution.length_of_last_word("fly me to the moon"))
print(solution.length_of_last_word("luffy is still joyboy"))
