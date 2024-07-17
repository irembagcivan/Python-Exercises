""" n=2, steps = 2
    n=3, steps = 3
    n=4, steps = 5
    n=5, steps = 8
    n=6, steps = 13 """
# so we can find a solution to this problem using fibonacci!

class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n==1:
            return 1
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)

solution = Solution()
print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(5))
print(solution.climbStairs(6))
