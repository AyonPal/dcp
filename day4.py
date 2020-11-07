"""
Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.
"""

class Decrement:
    def __init__(self, N):
        self.N = N
    
    def smallestFactor(self, n):
        return min([(i,n//i, abs((n//i)-i)) for i in range(1,n//2+1) if n%i==0], key= lambda t: t[2])

    def steps(self,current=None, steps=0):
        if current == None:
            current = self.N
        if current == 1:
            return steps
        else:
            # get factors with smallest dif and set next step the maximum
            sf = self.smallestFactor(current)
            maxFactor = max(sf[:-1])
            if maxFactor == current:
                # reduce by 1
                return self.steps(current-1,steps+1)
            else:
                return self.steps(maxFactor, steps+1)
                

if (__name__ == "__main__"):
    obj = Decrement(100)
    print(obj.steps())