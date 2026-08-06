class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        for st in s:
            if st in letters:
                return st
            else:
                letters.append(st)