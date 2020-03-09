'''
PROBLEM 5: NEW YEAR CHAOS PROBLEM

N NO. OF PERSON ARE STANDING IN QUEUE, IN ORDER WITH THERE POSITIONS AS STICKERS. 
NOW EACH PERSON CAN BRIBE TO SWAP PLACE WITH THE PERSON INFRONT OF HIM. BUT THERE POSITON STICKERS
REMAIN THE SAME. NOW GIVEN A QUEUE WITH POSITIONS WE NEED TO FIND THE MIN. NO. OF BRIBES TO REACH
THIS CURRENT STATE, IF NOT POSSIBLE PRINT 'TOO CHAOTIC'.

'''


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
