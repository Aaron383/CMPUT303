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
import math


line = sys.stdin.readline()
line = line[:len(line) - 1].split()
slices = int(line[0])
rings = int(line[1])
length = float(line[2])
line = sys.stdin.readline()
line = line[:len(line) - 1].split()
line = [int(x) for x in line]
a_x = line[0]
a_y = line[1]
b_x = line[2]
b_y = line[3]


straight_length = length/rings
distance = float(abs(a_y - b_y) * straight_length)
angle = abs(a_x - b_x)*(math.pi/slices)

if a_y <= b_y:
    if angle > 2:
        arc = straight_length * a_y * 2
    else:
        arc = straight_length * a_y * angle
else:
    if angle > 2:
        arc = straight_length * b_y * 2
    else:
        arc = straight_length * b_y * angle

distance = distance + arc

print('%.14f' % distance)



