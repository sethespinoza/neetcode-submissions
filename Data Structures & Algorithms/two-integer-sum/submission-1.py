class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # T: O(n), S: O(n)
        hasSeen = {} # val -> index
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hasSeen:
                return [hasSeen[difference], i]
            hasSeen[n] = i
        
        