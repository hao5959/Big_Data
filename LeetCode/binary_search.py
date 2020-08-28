class Solution:
    def binarySearch(self, nums, t):
        if not nums: return None
        l, r = 0, len(nums) - 1
        index = -1
        
        while l <= r:
            m = l + (r - l)//2
            if nums[m] == t:
                index = m
                break
            elif nums[m] < t:
                l = m + 1
            else: 
                r = m - 1
        print(index)
res = Solution()
res.binarySearch([-1, 0, 3, 5, 9, 12], 9)
