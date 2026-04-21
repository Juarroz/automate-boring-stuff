import random, sys, time
from idlelib.autocomplete import TRY_A

WIDTH = 70

try:
    # For each column, when the counter is 0, no stream is shown
    # otherwise, it acts as a counter for how many times a 1 or 0
    # should be display at that column
    columns = [0] * WIDTH
    while True:
        #loop over each column
        for i in range(WIDTH):
            if random.random() < 0.02:
                # Restart a stream counter on this column
                # The stream length is between 4 and 14 characters long.
                columns[i] += random.randint(4, 14)

            # print the character in this column
            if columns[i] == 0:
                # chance this ' '', to '.' to see the empty spaces
                print(' ', end='')
            else:
                #Print a 0 or 1
                print(random.choice([0, 1]), end='')
                columns[i] -= 1 # Decrements count for this column
        print() # Print a new line at the end of the row of columns
        time.sleep(0.2) # Each row pauses for the one tenth of a second
except KeyboardInterrupt:
    sys.exit() # when CTRL + c is pressed, end the program

