'''
PROBLEM: A RANSOM NOTE IS TO BE WRITTEN USING WORDS FROM A MAGAZINE.
GIVEN THE WORDS IN A MAGAZINE AND THE RANSOM NOTE TO BE WRITTEN. SOLUTION
REQUIRES TO PRINT YES OR NO IF ITS POSSIBLE TO WRITE THE RANSOM NOTE USING
WORDS FROM THE MAGAZINE.

EX.: MAGAZINE -> give me one grand today night
     NOTE     -> give one grand today

SOLN.: Yes

'''


class RansomNote():
    def __init__(self):
        m = 7
        n = 4

        magazine = 'give me one grand today night'
        note = 'give one grand today'

        result = self.Check(m, n, magazine, note)
        print(result)

    def Check(self, m, n, magazine, note):
        if (n > m):
            return 'No'

        mag_words = set(magazine.split(' '))
        note_words = set(note.split(' '))

        mag_words_count = {}

        for word in mag_words:
            mag_words_count[word] = magazine.count(word)

        for word in note_words:
            note_words_count = note.count(word)
            try:
                if (mag_words_count[word] < note_words_count):
                    return 'No'
            except KeyError:
                return 'No'

        return 'Yes'


RansomNote()
