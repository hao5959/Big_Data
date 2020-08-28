import heapq
class Test:
    def findKthLargest(self, nums, k):
        if not nums or not k or k < 0: None
        maxheap, res = [], None
        for num in nums:
            heapq.heappush(maxheap, -num)

        for _ in range(k):
            res = -heapq.heappop(maxheap)
        return res

li = Test()
print(li.findKthLargest([1, 2, 3, 8, 7, 4], 4))

