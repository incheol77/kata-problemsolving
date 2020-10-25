class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left <= right:
                mid = left + (right - left) // 2
                if target > nums[mid]:
                    return binary_search(mid + 1, right)
                elif target < nums[mid]:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)
