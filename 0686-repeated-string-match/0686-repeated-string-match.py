class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        temp = ""
        count = 0

        while len(temp) < len(b):
            temp += a
            count += 1

        if b in temp:
            return count
        elif b in (temp+a):
            return count+1
        else:
            return -1