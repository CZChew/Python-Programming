# This program will convert minutes to hours and minutes
# using the remaider

# Variable initialization: User input -> minutes_to_convert
minutes_to_convert = 1023

# Computation: Convert minutes to hours and minutes by parts
hours_part = int(minutes_to_convert/60)

# The remainder gives the number of minutes remaining
minutes_part = minutes_to_convert%60

# Display results: Hours and Minutes
print('Minutes to convert:',minutes_to_convert, 'minutes')
print('Hours:',hours_part)
print('Minutes:',minutes_part)
