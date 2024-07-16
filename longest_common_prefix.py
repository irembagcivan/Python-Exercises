class Solution():
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        
        shortest = min(strs, key = len) # Find the shortest string

        # Check every character of the shortest string
        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]:
                    # If any character is different, return the prefix up to that moment
                    return shortest[:i]
        # If no differences are found, the entire shortest string is the common prefix     
        return shortest


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flew", "flown"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))