class NewYearChaos():
    def __init__(self):
        q = [2, 1, 5, 3, 4]
        result = self.Solve(q)

        print(result)

    def Solve(self, q):
        bribe = 0
        chaotic = False
        l = len(q)

        for i in range(0, l):
            # if move is greater than 2 steps then queue is chaotic
            if(q[i]-(i+1) > 2):
                chaotic = True
                break

            # loop from current position to steps forward
            for j in range(max(0, q[i]-2), i):
                if (q[j] > q[i]):
                    bribe += 1

        if(chaotic):
            return 'Too chaotic'
        else:
            return bribe


NewYearChaos()
