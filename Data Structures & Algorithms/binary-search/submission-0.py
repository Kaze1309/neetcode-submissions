class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums) - 1
        l = 0
        mid = (l + h) // 2
        while l <= h:
            if target > nums[mid]:
                l = mid + 1
                mid = (l + h) // 2
            elif target < nums[mid]:
                h = mid - 1
                mid = (l + h) // 2
            else:
                return mid
        return -1
