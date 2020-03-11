'''
PROBLEM 7: ARRAY MANIPULATION

GIVEN LENGTH OF ARRAY OF ZEROS WITH INDEXES STARTING FROM 1 AND A MATRIX OF OPERATIONS. EACH OPERATION HAS A STARTING 
INDEX, ENDING INDEX AND VALUE THAT IS ADDED WITH CURRENT VALUE OF THAT INDEX. AFTER APPLYING ALL THE OPERATIONS THE MAX. 
VALUE IN THE ARRAY IS THE REQUIRED SOLUTION. 
EX:. 5 3
    [1, 2, 100]
    [2, 5, 100]
    [3, 4, 100]
    
SOLN.:  [0 0 0 0 0]
        [100 100 0 0 0]
        [100 200 100 100 100]
        [100 200 200 200 100]
        
RESULT: 200

'''


class ArrayManipulation():
    def __init__(self):
        n = 5
        queries = [[1, 2, 100],
                   [2, 5, 100],
                   [3, 4, 100]]

        result = self.MaxValue(n, queries)
        print(result)

    def MaxValue(self, n, queries):
        max_no = 0
        arr = [0] * (n+1)  # array with one extra space

        for i in range(0, len(queries)):
            start = queries[i][0]
            end = queries[i][1]
            val = queries[i][2]

            arr[start-1] = arr[start-1] + val  # add value to the index

            # subtract value from the index after the range
            arr[end] = arr[end] - val

        sum = 0
        for i in range(0, n):  # add the elements of the result array from left and find the max. value
            sum += arr[i]
            if (sum > max_no):
                max_no = sum

        return max_no


ArrayManipulation()
