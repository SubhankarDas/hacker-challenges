'''
PROBLEM 8: TWO STRINGS

GIVEN TWO STRINGS SOLUTION NEEDS TO FIND IF THE STRINGS HAVE A COMMON SUBSTRING.
A SUBSTRING CAN ALSO BE A SINGLE LETTER.

'''


class TwoStrings():
    def __init__(self):
        s1 = 'Hi'
        s2 = 'World'

        result = self.Substring(s1, s2)
        print(result)

    def Substring(self, s1, s2):
        set1 = set(s1)
        set2 = set(s2)

        print(set2)

        if (len(set1.intersection(s2)) > 0):
            return 'YES'
        else:
            return 'NO'


TwoStrings()
