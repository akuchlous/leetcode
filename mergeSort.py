#merge sort
#!/usr/bin/env python
import pdb;

def merge(list1, list2):
    retList = []
    #print (list1, list2)
    #pdb.set_trace()
    while ((len(list1)>0) and len(list2)>0):
        if list1[0] < list2[0]:
            retList.append(list1.pop(0))
        else:
            retList.append(list2.pop(0))
    #print(retList)
    if (len(list1) > 0):
            retList.extend(list1)
    if (len(list2)>0):
            retList.extend(list2)
    #print (retList)
    return retList

def mergeSort(list):
    mid = len(list)/2
    list1 = list[:mid]
    list2 = list[mid:]
    #print (list, list1, list2)
    if (len(list1)>=2):
        list1 = mergeSort(list1)
    if (len(list2)>=2):
        list2 = mergeSort(list2)
    return merge (list1, list2)


if __name__ == "__main__":
    list = [1]
    print (mergeSort(list))
    list = [2,1]
    print (mergeSort(list))
    list = [2,1,3]
    print (mergeSort(list))
    list = [2,1,3,34,12,43,44,1,2123,0]
    print (mergeSort(list))
