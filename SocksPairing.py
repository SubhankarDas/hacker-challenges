'''
PROBLEM 1: SOCK MERCHANT

GIVEN IS THE NO. OF SOCKS (N) AND INTEGER ARRAY CORRESPONDING TO THE COLOR OF THE SOCKS.
SOLUTIONS REQUIRES CALCULATING THE NO. OF PAIRS OF THESE SOCKS CAN BE FORMES ACCORDING TO MATCHING COLORS.

EX.: 1, 2, 1, 2, 1, 3, 2
SOLN.: 1 PAIR FOR COLOR 1, 1 PAIR FOR COLOR 2   ->  RESULT = 3
'''
class SocksPairing():
    def __init__(self):
        n = 9
        ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

        result = self.PairSocksByColor(n, ar)
        print(result)

    def PairSocksByColor(self, n, ar):
        count = {}
        total_pairs = 0

        for i in range(0, len(ar)):
            cur_count = count.get(ar[i])
            if (cur_count == None):
                count[ar[i]] = 1
            else:
                cur_count += 1
                count[ar[i]] = cur_count

        for k in count.keys():
            pair_count = int(count[k] / 2)
            total_pairs += pair_count

        return total_pairs


SocksPairing()
