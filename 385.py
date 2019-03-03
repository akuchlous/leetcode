class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        def recurse (s):
            if ("," not in s): return NestedInteger(int(s))
            r1, r2 = s[1:-1].split(",")
            return [recurse(r1), recurse(r2)]

        if s.replace("[", "").replace("]","") == ""  : return None
        if not s : return None
        return recurse(s)
