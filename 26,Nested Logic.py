# Objective
# Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing.

# Task
# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

# If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
# If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
# If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
# Example
#  returned date
#  due date

# The book is returned on time, so no fine is applied.

#  returned date
#  due date

# The book is returned in the following year, so the fine is a fixed 10000.

# Input Format

# The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned.
# The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due date).

# Constraints

# Output Format

# Print a single integer denoting the library fine for the book received as input.

# Sample Input

# STDIN       Function
# -----       --------
# 9 6 2015    day = 9, month = 6, year = 2015 (date returned)
# 6 6 2015    day = 6, month = 6, year = 2015 (date due)
# Sample Output

# 45
# Explanation

# Given the following return dates:
# Returned: 
# Due: 

# Because , it is less than a year late.
# Because , it is less than a month late.
# Because , it was returned late (but still within the same month and year).

# Per the library's fee structure, we know that our fine will be . We then print the result of  as our output.
dmy=[int(x) for x in input().split(' ')]
dmy2=[int(x) for x in input().split(' ')]
if (dmy[-1]==dmy2[-1]):
    if(dmy[-2]<=dmy2[-2]):
        if(dmy[0]<=dmy2[0]):
            print(0)
        else:
            print(abs(dmy[0]-dmy2[0])*15)
    else:
        print(abs(dmy[1]-dmy2[1])*500)
elif(dmy[-1]<dmy2[-1]):
    print(0)
else:
    print(10000)
