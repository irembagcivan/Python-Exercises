class Solution():
    def contains_duplicate(self,nums):
        char_nums = {}

        for num in nums:
            if num in char_nums:
                return True
            
            char_nums[num] = 1

        return False
                
            
solution = Solution()
print(solution.contains_duplicate([1,2,3,4]))
print(solution.contains_duplicate([1,2,3,1]))
print(solution.contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
