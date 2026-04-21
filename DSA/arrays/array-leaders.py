class Solution:
    def leaders(self, arr):
            output_array = []
            
            max_so_far = float('-inf')
            
            for i in range(len(arr)-1, -1, -1):   # right → left
                if arr[i] >= max_so_far:
                    output_array.append(arr[i])
                    max_so_far = arr[i]
            
            return output_array[::-1]   # reverse to correct order


obj = Solution()
print(obj.leaders([16,17,4,3,5,2]))