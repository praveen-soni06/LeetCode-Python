def floor(arr, x):
    s,e = 0, len(arr)-1
    ans = 0
    while s<=e:
        m = (s+e)//2
        if arr[m] <= x:
            ans = m
            s = m + 1
        else:
            e = m - 1
    return ans

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        i = floor(arr, x)
        j = i + 1
        ans = []

        while k>0 and i>=0 and j<len(arr):
            if abs(x-arr[i]) <= abs(x-arr[j]):
                ans.append(arr[i])
                i -= 1
            else:
                ans.append(arr[j])
                j += 1
            k -= 1
        
        while k>0 and i>=0:
            ans.append(arr[i])
            i -= 1    
            k -= 1

        while k>0 and j<len(arr):
            ans.append(arr[j])
            j += 1    
            k -= 1           
        
        return sorted(ans)