class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T: O(n), S: O(n)
        
        hasSeen = set()
        for n in nums:
            if n in hasSeen:
                return True
            hasSeen.add(n)
        return False

        