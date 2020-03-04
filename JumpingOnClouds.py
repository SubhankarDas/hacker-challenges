'''
PROBLEM 3: JUMPING ON THE CLOUDS

EMMA JUMPS ON CLOUDS WHERE CLOUDS WITH 0 IS SAFE AND 1 IS UNSAFE. SHE CAN EITHER TAKE 1 STEP OR 2 STEPS AT A TIME.
SOLUTION REQUIRES MIN. NO. OF STEPS REQUIRED TO REACH THE END OF THE CLOUDS SAFELY.

EX.: 7
    0 0 1 0 0 1 0
RESULT: 4

'''


class JumpingOnClouds():
    def __init__(self):
        c = [0, 0, 1, 0, 0, 1, 0]  # clouds [ 0 = safe   1 = unsafe ]
        result = self.Jump(c)

        print(result)

    def Jump(self, c):
        cur_step = 0  # current step
        step_count = 0  # steps count

        while (cur_step < (len(c)-1)):  # loop till 2nd last cloud
            step_1 = 0
            step_2 = 0

            if (cur_step + 1 < len(c)):  # if 1 step is not end store step value
                step_1 = c[cur_step + 1]
            if (cur_step + 2 < len(c)):  # if 2 steps is not end store step value
                step_2 = c[cur_step + 2]

            if (step_2 == 0):  # if 2 steps is safe, take 2 steps and step count
                step_count += 1
                cur_step += 2

                continue
            elif (step_1 == 0):  # else if 1 steps is safe, take 1 step and step count
                step_count += 1
                cur_step += 1

                continue

        return step_count


JumpingOnClouds()
