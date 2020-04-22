'''
PROBLEM: CLOCKWISE SPIRAL ARRAY TRAVERSAL

SOLUTION: TRAVERSE MATRIX AS SPIRALS I.E FIRST OUTER MOST CIRCLE THEN INNER CIRCLE AND SO ON.
FIND THE DIAGONAL ENDS I.E CORNER 1 AND CORNER 2 THEN FOR CLOCKWISE TRAVERSAL LOOP TO RIGHT, DOWN, 
THEN LEFT AND FINALLY UP. THEN MOVE TO THE INNER CIRCLE AND CONTINUE TILL INSIDE.
 
'''


class MatrixClockSpiral():
    def __init__(self):
        # arr = [[1, 2, 3, 4],
        #        [12, 13, 14, 5],
        #        [11, 16, 15, 6],
        #        [10, 9, 8, 7]]

        arr = [[1, 2, 3, 4, 5],
               [16, 17, 18, 19, 6],
               [15, 24, 25, 20, 7],
               [14, 23, 22, 21, 8],
               [13, 12, 11, 10, 9]]

        self.ClockwiseSpiral(arr)

    def ClockwiseSpiral(self, arr):
        n = len(arr)  # array length

        diag = int(n / 2) + n % 2  # diagonal = corner 1

        # loop within inner circles
        for i in range(0, diag):
            diag_end = n - i - 1  # diagonal end = corner 2

            for j in range(i, diag_end):  # right traversal
                print(arr[i][j], end=" ")

            for j in range(i, diag_end):  # down traversal
                print(arr[j][diag_end], end=" ")

            for j in range(diag_end, i, -1):  # left traversal
                print(arr[diag_end][j], end=" ")

            for j in range(diag_end, i, -1):  # up traversal
                print(arr[j][i], end=" ")

        if (n % 2):  # corner case for odd length
            print(arr[diag_end][diag_end])


MatrixClockSpiral()
