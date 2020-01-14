"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# Create the program.

def return_cal():
  
  # Create a variable to define the arguments inputted.
  # sys.argv returns a list.
  
  input = sys.argv

  # If no arguments specified, print a calendar for the current month.
  
  if len(input) == 1:
    y = datetime.now().year
    m = datetime.now().month
    print(calendar.month(y, m))
  
  # If one argument specified, assume month was passed 
  # and return the calendar for that month and the current year.

  elif len(input) == 2:
    y = datetime.now().year
    m = int(input[1])
    print(calendar.month(y, m))

  # If two arguments specified, assume they passed both the month and year
  # and return the calendar for that month and year.

  elif len(input) == 3:
    y = int(input[2])
    m = int(input[1])
    print(calendar.month(y, m))

  # Else print a statement that indicates the format your program expects
  # arguments to be given. Then exit the program.

  else:
    print("Please only input one number to indicate month followed by the desired year.")
    exit()

# Execute the code in the file.

if __name__ == "__main__":
  return_cal()