# This program will convert minutes to hours and minutes
# using the remaider

# Program Introduction
print('A simple program to convert minutes into hours and minutes')
print('----------------------------------------------------------')

# Variable initialization: User input -> minutes_to_convert
minutes_to_convert = int(input('Minute to convert: '))

# Computation: Convert minutes to hours and minutes by parts
hours_part = int(minutes_to_convert/60)

# The remainder gives the number of minutes remaining
minutes_part = minutes_to_convert%60

# Display results: Hours and Minutes
print('Conversion results: ' + str(hours_part) + ' Hours ' + str(minutes_part) + ' Minutes')

