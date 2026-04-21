class Solution:
    def secondLargest(self,arr):
        try:
            s = set(arr)
            s.remove(max(s))
            return max(s)
        except Exception as e:
            return -1
sol = Solution()
print(sol.secondLargest([10, 10, 10]))
# output should be 34