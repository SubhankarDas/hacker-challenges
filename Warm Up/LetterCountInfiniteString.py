'''
PROBLEM 4: COUNT THE NO. OF A IN SUBSTRING OF AN INFINITE REPEATING STRING.

S = ABCAC    I.E INFINITE STRING IS FORMED REPEATING S STRING.
N = 10       I.E EXTRACT SUBSTRING OF N LENGTH FROM INFINITE STRING

STRING  = ABCACABCAC

RESULT: 4

'''


class LetterCountInfiniteString():
    def __init__(self):
        s = 'aba'
        n = 10

        result = self.Count(s, n)
        print(result)

    def Count(self, s, n):
        total_count = 0
        count = s.count('a')  # count no. of a in given string
        l = len(s)  # length of string

        # repeating no. of strings in the substring length
        repeating_len = int(n/l)
        remaining_len = n % l  # remaining length of the substring

        total_count = repeating_len * count  # no. of a in repeating strings

        substr = s[0: remaining_len]  # extract substring from remaining length

        # add count of a in the remaining substring
        total_count += substr.count('a')

        return total_count


LetterCountInfiniteString()
