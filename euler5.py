import itertools
import pdb

def euler(m):
    """Yield tuples (a, b, c, d, e) such that a^5 + b^5 + c^5 + d^5 = e^5,
    where all are integers, and 1 < a ≤ b ≤ c ≤ d < e < m."""
    powers = [e**5 for e in range(2, m)] 
    pairs  = {sum(pair): pair 
              for pair in itertools.combinations_with_replacement(powers, 2)}
    for pair1 in pairs:
        for e5 in powers:
            pair2 = e5 - pair1
            if pair2 in pairs:
                fifthroots(pairs[pair1] + pairs[pair2] + (e5,))
    
def fifthroots(nums): 
    "Sorted integer fifth roots of a collection of numbers." 
    pdb.set_trace()
    print (tuple(sorted(int(round(x ** (1/5))) for x in nums)))


euler (500)
