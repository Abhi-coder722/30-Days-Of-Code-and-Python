# You are given a positive integer .
# Your task is to print a palindromic triangle of size .

# For example, a palindromic triangle of size  is:

# 1
# 121
# 12321
# 1234321
# 123454321
# You can't take more than two lines. The first line (a for-statement) is already written for you.
# You have to complete the code using exactly one print statement.

# Note:
# Using anything related to strings will give a score of .
# Using more than one for-statement will give a score of .

# Input Format

# A single line of input containing the integer .

# Constraints

# Output Format

# Print the palindromic triangle of size  as explained above.

# Sample Input

# 5
# Sample Output

# 1
# 121
# 12321
# 1234321
# 123454321
n=int(input());t=0
for i in range(n): t=10*t+1;print(t*t);
