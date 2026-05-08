class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T: O(n), S: O(n)
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
    
        