# Objective
# Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.

# Example

# The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, .

# Input Format

# A single integer, .

# Constraints

# Output Format

# Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .

# Sample Input 1

# 5
# Sample Output 1

# 1
# Sample Input 2

# 13
# Sample Output 2

# 2
# Explanation

# Sample Case 1:
# The binary representation of  is , so the maximum number of consecutive 's is .

# Sample Case 2:
# The binary representation of  is , so the maximum number of consecutive 's is .
#!/bin/python3

import math
import os
import random
import re
import sys

# // import java.io.*;
# // import java.math.*;
# // import java.security.*;
# // import java.text.*;
# // import java.util.*;
# // import java.util.concurrent.*;
# // import java.util.regex.*;



# // public class Solution {
# //     public static void main(String[] args) throws IOException {
# //         Scanner sc = new Scanner(System.in);
# //         int n = sc.nextInt();
# //         String[] groupings= Integer.toBinaryString(n).split("0");
# //         int max=0;
# //         System.out.println(groupings[1]);
# //         for(String s : groupings){
# //             if (max<s.length()){
# //                 max=s.length();
# //             }
# //         }
# //         System.out.println(max);
# // }
# // }


if __name__ == '__main__':
    n = int(input().strip())
    n=bin(n)[2:]
    n=n.split('0')
    n=[len(i) for i in n]
    print(max(n))
