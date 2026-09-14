class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # applying KMP Algorithm to solve this problem
        # in KMP least prefix suffix(LPS) are use
        # lps store the repeated char last positin 
        # ex needle = AAAA, so lps = [0,1,2,3]

        if needle == "": return 0
        if len(needle) > len(haystack): return -1

        lps = [0] * len(needle)

        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS+1
                i += 1
                prevLPS += 1

            elif prevLPS == 0:    # checking if prevLPS is 0 then store that posi is 0 and searching next element 
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]  # increment ang go to that position char of needle

        # now for matchin with haystack and finding first occurance position
        i = 0  # for haystack
        j = 0  # for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            else:
                if j == 0:   # stop for stockin at one position
                    i += 1
                else:
                    j = lps[j - 1]  # decs at one position
            
            if j == len(needle):
                return i - len(needle)  # calculating exact first occ posi

        return -1