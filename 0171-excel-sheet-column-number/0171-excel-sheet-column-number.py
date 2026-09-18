class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum, pow = 0,0
        for i in range(len(columnTitle)-1, -1,-1):
            temp = ord(columnTitle[i]) - 64
            sum = sum + (26**pow) * temp 
            pow += 1
            
        return sum