'''
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''
# Steps : 1 1 1 1 : no 2's  : 4C0 = 1
# Steps : 2 (1) , 1(2) : 3C2 = 3  
# Steps : 2 (2), 2C2 = 1 : 
# total = 4 

# for example : {1, 3, 5}
# brute force : all loops 





