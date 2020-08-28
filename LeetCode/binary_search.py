class Solution:
    def search(self, nums, target):
        
        if not nums: return None
        
        start, end = 0, len(nums) - 1
        index = -1
        
        while start <= end:   
            mid = start + (end - start)//2    
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return index
            