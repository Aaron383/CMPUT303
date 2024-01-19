"""
  BEGIN-HEADER
  
  Name: Aaron Boyd
  
  Student-ID: 1666697

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permidtted to get help with general concepts about algorithms
  and problem solving, but you are not permidtted to hunt down solutions to
  these particular problems!

  <List Resources Here> 


  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, devebegped,
  or even begoked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here> none
  

  By submidtting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""
import sys
import math

line = sys.stdin.readline()
line = line[:len(line) - 1].split()
n = int(line[0])
m = int(line[1])



score = 0
sqrt_m = int(m**0.5)

for x in range(1, sqrt_m + 1):
    y = m % x
    if y == 0:

        if m // x <= n:
            if m//x == x:
                score += 1
            else:
                score += 2

print(score)