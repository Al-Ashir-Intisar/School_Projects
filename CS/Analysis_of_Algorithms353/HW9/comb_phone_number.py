class Solution:
    def letterCombinations(self, digits):
        digits_d = {'2':['a','b','c'], 
        '3':['d','e','f'],
        '4':['g','h','i'], 
        '5':['j','k','l'], 
        '6':['m','n','o'], 
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
        }
        res = []
        def find_n(ind,sub):
            if len(sub) ==len(digits):
                res.append(sub[:])
                return
            # if ind >= len(digits):
            #     return 
            dig = digits_d[digits[ind]]
            for i in dig:
                sub.append(i)
                find_n(ind+1,sub)
                sub.pop()
        
        if len(digits) >0:
            find_n(0,[])
        else:
            return []
        res1 = []
        for i in res:
            res1.append("".join(i))
        return res1
    

solution = Solution()
digits = "2445"
result = solution.letterCombinations(digits)
print(result)