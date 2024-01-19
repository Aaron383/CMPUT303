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

n = int(input())
passwords = []
ans = 0.0
for i in range(n):

    line = sys.stdin.readline()
    line = line[:len(line) - 1].split()
    prob = float(line[1])
    passwords.append(prob)

passwords.sort(reverse=True)
for i in range(n):
    ans += passwords[i] * (i+1)

print(f"{ans:.4f}")
