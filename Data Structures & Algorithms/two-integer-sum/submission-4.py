class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # T:O(n), S:O(n)
        hasSeen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hasSeen:
                return [hasSeen[diff], i]
            hasSeen[n] = i

        