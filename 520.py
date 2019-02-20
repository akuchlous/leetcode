#!/usr/bin/env python

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return (word.islower() or word.isupper()) or (str[0].isupper and str[1:].islower())


print (Solution().detectCapitalUse("FlaG"))
