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


import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split()
num = int(line[0])
div = int(line[1])
line = sys.stdin.readline()
line = line[:len(line) - 1].split()
numbers = [int(x) for x in line]


dictionary = {}
sum = 0

for x in numbers:
    if x//div in dictionary:
        dictionary[x//div] += 1
    else: 
        dictionary[x//div] = 1

num = 0
for x in dictionary.values():
    num += x*(x-1)
print(num//2)
