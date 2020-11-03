"""
This problem was asked by Epic.

The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""


class LookAndSay:

    def __init__(self, N):
        self.N = N
        self.START = "1"

    def next_term(self, current_term):
        next_seq = ""
        count = 0
        last = current_term[0]
        for c in current_term:
            # Count similar numbers
            if(c == last):
                count += 1
            # Update if new number found
            else:
                next_seq += str(count) + last
                count = 1
                last = c
        else:
            # Add last item left
            next_seq += str(count) + last
        return next_seq

    def calculate(self):
        next_seq = self.next_term(self.START) if self.N > 1 else self.START
        # first term is already calculated or given so skip 1 term (N-2 instead N-1)
        for i in range(self.N-2):
            next_seq = self.next_term(next_seq)
        return next_seq


if (__name__ == "__main__"):
    N = 6
    obj = LookAndSay(N)
    print(f'The {N} term is {obj.calculate()}')
