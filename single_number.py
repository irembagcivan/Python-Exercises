class Solution(object):
    def single_number(self,nums):
        for i in range(len(nums)):
            single = True
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    single = False
                    break
            if single:
                return nums[i]
        
solution = Solution()
print(solution.single_number([2,2,1]))
print(solution.single_number([4,1,2,1,2]))
print(solution.single_number([1]))

