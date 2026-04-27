"""You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Input : arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.
"""

class Solution:
    def missingNum(self,arr):
        # my approach
        # max_num = max(arr)
        # for i in range(1,max_num+2):
        #     if(i in arr):
        #         continue
        #     else:
        #         return i 
        # correct approach
        n = len(arr) + 1
        expected = n*(n+1)//2
        actual = sum(arr)
        return expected-actual
sol = Solution()
print(sol.missingNum([1]))