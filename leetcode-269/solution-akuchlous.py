#!/usr/bin/env python


def al(order, words):
    dic = {}
    i = 1
    for o in order:
        dic[o] = i
        i = i+1
    for x in range(0, len(words[0])):
        minV  = 0
        for w in words:
            if (minV > dic[w[x]]):
                return False
            minV = dic[w[x]]
   
    return True

order = ["c", "a", "b"]
words = ["abc", "cab"]
print (al(order, words))
words = ["c", "c"]
print (al(order, words))
words = ["cab", "caa"]
print (al(order, words))
words = ["caa", "cab"]
print (al(order, words))
