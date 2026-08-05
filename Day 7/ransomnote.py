class Solution:
    def canConstruct(self, ransomNote, magazine):
        count = [0] * 26
        
        for ch in magazine:
            count[ord(ch) - ord('a')] += 1
        
        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False
        
        return True