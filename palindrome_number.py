class Solution():
    def palindrome_num(self,num):
        if num < 0:
            return False
        
        number = str(num)
        reversed_number = number[::-1]

        if reversed_number == number:
            return True
        else:
            return False
            

solution = Solution()
print(solution.palindrome_num(121))
print(solution.palindrome_num(-121))
print(solution.palindrome_num(222))
print(solution.palindrome_num(345))
