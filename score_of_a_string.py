# ord() fonksiyonu verilen tek karakterlik bir stringin tam sayı değerini döndürür. Bu, karakterin ASCII (veya Unicode) değerine karşılık gelir.

class Solution():
    def score_string(self,word):
        score = 0
        for i in range(len(word) - 1):
            score += abs(ord(word[i+1]) - ord(word[i]))
        return score

solution = Solution()
print(solution.score_string("hello"))
print(solution.score_string("zaz"))