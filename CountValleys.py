'''
PROBLEM 2: COUNTING VALLEYS

A HIKER RECORDS HIS STEPS DURING A HIKE, N IS THE NO. OF STEPS IN A HIKING TRIP.
S IS A SEQUENCE OF STEPS WHERE U REPRESENTS UP STEP AND D REPRESENTS DOWN STEP.
STARTING FROM SEA LEVEL HIKER ENDS TRIP AFTER RETURNING TO SEA LEVEL ONLY.
REQUIRED COUNT THE NO. OF VALLEYS DURING A HIKE, WHERE A VALLEY IS SEQUENCE OF CONSECUTIVE
STEPS BELOW SEA LEVEL AND ENDS WITH A STEP UP TO SEA LEVEL.
EX.: 8
     UDDDUDUU
RESULT: 1

_/\      _
   \    /
    \/\/
    
'''
class CountValleys():
    def __init__(self):
        n = 12
        s = 'DDUUDDUDUUUD'

        result = self.Count(n, s)
        print(result)

    def Count(self, n, s):
        val_count = 0
        cur_alt = 0

        in_valley = 0

        for i in range(0, n):
            step = s[i]
            if (step == 'U'):
                cur_alt += 1
            else:
                cur_alt -= 1

            if (in_valley == 1 and cur_alt == 0):
                val_count += 1

            if (cur_alt < 0):
                in_valley = 1
            else:
                in_valley = 0

        return val_count


CountValleys()
