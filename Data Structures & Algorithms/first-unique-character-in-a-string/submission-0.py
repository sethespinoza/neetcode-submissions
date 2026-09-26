class Solution:
    def firstUniqChar(self, s: str) -> int:
        # T: O(n), S: O(1) at most 26 chars
        counts = {}
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1

        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1



        