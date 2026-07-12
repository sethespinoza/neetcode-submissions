class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # T: O(n), S: O(n)
        hasSeen = {} # val to index
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hasSeen:
                return [hasSeen[complement], i]
            hasSeen[n] = i
        
        