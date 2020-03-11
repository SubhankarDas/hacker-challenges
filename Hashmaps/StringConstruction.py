'''
PROBLEM 9: STRING CONSTRUCTION

GIVEN A STRING S, SOLUTION REQUIRES TO COPY S TO A NEW STRING BASED ON SOME OPERATIONS AT A COST.
1. COPY LETTER FROM S TO P COSTS 1 DOLLAR
2. APPENDING A SUBSTRING FROM S TO END OF P COST NOTHING I.E 0
FIND THE TOTAL COST TO COPY S TO P.

EX: abcd -> 4 [COPY ALL THE LETTERS COST 1 DOLLARS]
    abab -> 2 [COPY A AND B COST 2 DOLLARS, APPENDING SUBSTRING AB COSTS NOTHING I.E TOTAL 2 DOLLARS]

'''


class StringConstruction():
    def __init__(self):
        s = 'abab'

        result = self.Construct(s)
        print(result)

    def Construct(self, s):
        return len(set(s))


StringConstruction()
