class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # basic version 

        # stri = ""
        # for i in digits:
        #     stri += str(i)
        
        # temp = str(int(stri)+1)
        # res = []
        # for i in temp:
        #     res.append(int(i))
        # return res

        # improved version
        
        nums = 0
        for digit in digits:
            nums = nums*10+digit

        nums += 1
        ans = []
        while nums>0:
            temp = nums % 10
            ans.append(temp)
            nums //= 10

        return ans[::-1]
        