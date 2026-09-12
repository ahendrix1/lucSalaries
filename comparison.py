import pandas as pd
import numpy as np

# for the part time salary, I'm billing at a rate of (2590.73 + 2340.39) / 2
# per credit hour, which is the average of what seems to be the standard rates
# for prof. with terminal + non-terminal degrees, respectively. max credit
# hours is 18 a year, as per the adjunct + aca document on the luc. website
# values one credit hour as three work hours.
# all admin salaries are billed at 40 hours a week.

# when n credit hours is an integer such that 
# 1<=n<=6, n((2590.73 + 2340.39) / 2) = y, 
# where y is the amount of money made in one semester. 
# when 16 weeks is a semester, 3n is the equivalent to the work hours per
# week, y is as described above, and x is the estimated hourly wage, let
# y / (16 * 3n) = x.
# (n((2590.73 + 2340.39) / 2)) / (16 * 3n) = x
# n(2465.56) / (48n) = x

semWages = 2465.56
semHours = 48

hourly = 0
semester = []
yearly = []
admin = []

n = 1 

hourly = ((n * semWages) / (n * semHours))

csv = pd.read_csv("admin_out.csv")
admin = csv["salary"]

while n <= 6:
    semester.append(n * 2465.56)
    yearly.append(3 * n * 2465.56)
    n += 1

### ASSIGNMENT







