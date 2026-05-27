class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T: O(n), S: O(n)
        hasSeen = set()
        for num in nums:
            if num in hasSeen:
                return True
            hasSeen.add(num)
        return False
        