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

import heapq

def checkAnswer(p, orders, skipDays):
  move_i = 0
  end_times = []
  for day in range(1, 101):
      while move_i < len(orders) and orders[move_i][0] <= day:
          heapq.heappush(end_times, orders[move_i][1])
          move_i += 1
      if day % 7 not in skipDays:
          for _ in range(p // 2):
              if not end_times:
                  break
              heapq.heappop(end_times)
      if end_times and end_times[0] <= day:
          return False
      if not end_times and move_i == len(orders):
          break
  return True


n = int(input())

for x in range(n):
    line = sys.stdin.readline()
    line = line[:len(line) - 1].split()
    m = int(line[0])
    p = int(line[1])
    orders = []

    for piano in range(m):

      line = sys.stdin.readline()
      line = line[:len(line) - 1].split()
      b = int(line[0])
      e = int(line[1])

      orders.append((b, e))

    orders.sort()

    if checkAnswer(p, orders, {0, 6}):
        print("fine")
    elif checkAnswer(p, orders, set()):
        print("weekend work")
    else:
        print("serious trouble")



        