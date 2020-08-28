# method 1
class Solution:
    def searchRange(self, nums, target):
        result = [-1, -1]
        result[0] = self.findStartingIdx(nums, target)
        result[1] = self.findEndingIdx(nums, target)
        return result

    def findStartingIdx(self, nums, target):
        index = -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                index = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return index

    def findEndingIdx(self, nums, target):
        index = -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                index = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1 
        return index

llist = Solution()
print(llist.searchRange([5, 7, 7, 8, 8, 10], 8))

# method 2 