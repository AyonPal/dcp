"""
MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
"""


class MegaCorp:
    def __init__(self, arr):
        self.loc = arr
# Sol 1:
    # get all ascending chunks left to right
    def get_chunks(self):
        chunks = []
        current_chunk = []
        for i in self.loc:
            if len(current_chunk) == 0 or current_chunk[-1] < i:
                current_chunk.append(i)
            else:
                chunks.append(current_chunk)
                current_chunk = []
                current_chunk.append(i)
        else:
            chunks.append(current_chunk)
        return chunks

    def get_bonus(self):
        chunks = self.get_chunks()
        bonuses = []
        # convert each chunk to min bonus amount individual
        for c in range(len(chunks)):
            bonus= list(range(len(chunks[c])))
            bonuses.append(bonus)
        # update single chunks recursively right to left  and one multi chunk if any
        for b in range(len(bonuses)):
            if(len(bonuses[b])==1 and b!= len(bonuses)-1):
                i=b
                while(i>=0):
                    if(len(bonuses[i])!=1):
                        # update last element of multi chunk if needed and stop
                        bonuses[i][-1] += 0 if bonuses[i][-1]> bonuses[i+1][-1] else 1
                        i=0
                    else:
                        # update single chunk
                        bonuses[i][-1]+=1
                    i-=1
        return [b+1 for bonus in bonuses for b in bonus]
# Sol: 2
 # Get desc numbers
    def getRight(self, startIndex):
        count = 0
        arr  = self.loc[startIndex:]
        for i,num in enumerate(arr):
            if i<len(arr)-1 and arr[i+1]<num:
                count += 1
            else:
                return count+1
        return count+1

    
    # Solution doesn't work if have equal values
    def solve(self):
        result = []
        i = 0
        count = 0
        while(i<len(self.loc)):
            count += 1
            # get asc numbers
            if self.loc[i-1] < self.loc[i] or i-1 == -1:
                result.append(count)
                i += 1
            else:
                right = self.getRight(i)
                left = result[-1]
                if left < count < right:
                    # if this is top take max of both side
                    result.append(max(count,right))
                else:
                    # if this is slope take min of both side
                    result.append(min(count,right))
                # add descendings
                result+=[r+1 for r in list(range(right-1))[::-1]]
                count = 1
                i += right
        return result
        
if (__name__ == "__main__"):
    loc = MegaCorp([10, 40, 200, 1000, 60, 30])
    print(loc.solve())
            