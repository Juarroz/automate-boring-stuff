today_is_opposite_day = False

# Set say_is_opposite_day based on today_is_opposite_day
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

# if it is opposite day, toggle say_it_is_opposite_day:
if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day

# say what day it is:
if say_it_is_opposite_day == True:
    print('Today is Opposite Day')
else:
    print('Today is not Opposite Day')
