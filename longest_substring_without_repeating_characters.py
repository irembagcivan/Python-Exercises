class Solution():
    def longest_sub(self,s):
        all_substring = []
        substring = ""

        length = len(s)

        for i in range(length):
            if s[i] in substring:
                all_substring.append(substring)
                substring = ""

            substring += s[i]
            
        all_substring.append(substring)
        
        longest_substring = max(all_substring, key=len)
        return longest_substring

        

solution = Solution()
print(solution.longest_sub("abcabcbb"))
print(solution.longest_sub("bbbb"))
print(solution.longest_sub("pwwkew"))
print(solution.longest_sub("abcdef"))
