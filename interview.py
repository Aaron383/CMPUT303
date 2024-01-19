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
line = sys.stdin.readline()
queue = line[:len(line) - 1].split()
r = []

done = False
ans = 0
while not done:
    removed = []
    newQueue = []



    for i in range(len(queue)):
        if len(queue) == 1:
            newQueue.append(int(queue[i]))

        elif i == 0:
            if queue[i+1] > queue[i]:
                removed.append(int(queue[i]))
            else:
                newQueue.append(int(queue[i]))

        elif i == len(queue)-1:
            if queue[i-1] > queue[i]:
                removed.append(int(queue[i]))
            else:
                newQueue.append(int(queue[i]))

        elif queue[i-1] > queue[i] or queue[i+1] > queue[i]:
            removed.append(int(queue[i]))

        else:
            newQueue.append(int(queue[i]))

    if len(removed) == 0:
        done = True
        r.append(queue)
    else:
        ans += 1
        queue = newQueue
        r.append(removed)

print(ans)
for x in r:
    print(*x)

