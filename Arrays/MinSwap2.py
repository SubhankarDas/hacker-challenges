'''
PROBLEM 6: MIN. NO. OF SWAPS TO SORT IN ASCENDING ORDER

GIVEN AN ARRAY OF UNSORTED CONSECUTIVE NUMBERS I.E 1,2,3...,N WHERE N IS THE LENGTH OF THE ARRAY.
SOLUTION NEEDS TO FIND THE MIN. NO. OF SWAPS BETWEEN TWO NUMBERS TO SORT THE ARRAY IN ASCENDING
ORDER. THERE ARE NO DUPLICATES IN THE ARRAY.

EX.: 4 3 1 2
RESULT: 3

'''


class MinSwap2():
    def __init__(self):
        arr = [7, 1, 3, 2, 4, 5, 6]
        result = self.Swap(arr)

        print(result)

    def Swap(self, arr):
        swap_count = 0
        l = len(arr)
        val = {}
        pos = {}

        for i in range(0, l):

            # actual position doesn't match ideal position
            if ((i+1) != arr[i]):
                val[i+1] = arr[i]  # map of position -> value
                pos[arr[i]] = i + 1  # map of value -> position

        for i in val.keys():  # loop through elements need to be swapped
            cur_val = val[i]  # get current value
            find_val = i  # value to be swapped with
            swap_pos = pos[find_val]  # position to be swapped with

            # need to swap i.e position -> value -> position doesn't match
            if (i != swap_pos):
                pos[cur_val] = swap_pos  # update position array
                val[swap_pos] = cur_val  # update value array
                swap_count += 1

        return swap_count


MinSwap2()
