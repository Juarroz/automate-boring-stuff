import time, sys

indent = 0 # How many spaces to indent
indent_increasing = True # Whether the indentation is increasin or not

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10th second

        if indent_increasing:
            # increase the number of spaces:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            # Decrease the number of spaces
            indent -= 1
            if indent == 0:
                # Change direcction
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()

