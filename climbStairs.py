'''
A child climb stairs, she can climb either 1,  2 or 3 steps a time. How many ways to climb n stair
'''

def climbStairs(n):
    if n <= 2:
        return n
    return f(n-1) + f(n-2) + f(n-3)
    
