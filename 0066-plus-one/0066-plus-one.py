class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        stri = ""
        for i in digits:
            stri += str(i)
        
        temp = str(int(stri)+1)
        res = []
        for i in temp:
            res.append(int(i))
        return res
        