"""
  BEGIN-HEADER
  
  Name: Aaron Boyd
  
  Student-ID: 1666697

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here> none

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here> none
  

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

numbers.sort(reverse=True)

hindex = 0

for i in range(n):

    if numbers[i] >= i + 1:

        hindex = i + 1
    else:
        break

print(hindex)

