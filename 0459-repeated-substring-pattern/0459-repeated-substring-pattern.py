class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        lps = [0] * len(s)
        prevLPS, i = 0, 1

        while i < n:
            if s[i] == s[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1

            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        p_len = n - lps[n-1]   # finding substring length
        return lps[n-1] > 0 and n % p_len == 0  # check present in string