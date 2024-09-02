# Kadane's Algorithm

class Solution:
    def max_sub_array(self, nums):
        max_current = max_global = nums[0]
        
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current
        
        return max_global

solution = Solution()
print(solution.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))