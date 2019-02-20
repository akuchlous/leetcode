from collections import defaultdict
import pdb

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        countD = defaultdict(int)
        for cp in cpdomains:
            (count, domains) = cp.split(" ")
            countD[domains]+=int(count)
            for i in range(0, len(domains)):
                c = domains[i]
                if (c == "."):
                    countD[domains[i+1:]]+=int(count)
        return [str(countD[k]) + " " + str(k) for k in countD.keys()]    

print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

