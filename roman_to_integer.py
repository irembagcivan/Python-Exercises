class Solution(object):
    def romanToInt(self, s):
        roman_to_integer = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        n = len(s)
        sonuc = 0

        for i in range(n):
            if i < n-1 and roman_to_integer[s[i]] < roman_to_integer[s[i + 1]]:
                sonuc -= roman_to_integer[s[i]]

            else:
                sonuc += roman_to_integer[s[i]]
        return sonuc

solution = Solution()

print(solution.romanToInt("IV"))
print(solution.romanToInt("VI"))
print(solution.romanToInt("MCMXCIV"))  

