class Solution():
    def remove_duplicates(self,nums):
        new_nums = []

        for i in range(len(nums)):
            if nums[i] not in new_nums:
                new_nums.append(nums[i])
    
        return new_nums


solution = Solution()
print(solution.remove_duplicates([1,1,2]))
print(solution.remove_duplicates([0,0,1,1,1,2,2,3,3,4]))
print(solution.remove_duplicates([1,2,4]))
