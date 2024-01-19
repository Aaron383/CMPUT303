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

X = {}
Y = {}
xs = []
ys = []

# read points
for point in range(n):
    line = sys.stdin.readline()
    line = line[:len(line) - 1].split()
    x = int(line[0])
    y = int(line[1])

    xs.append(x)
    ys.append(y)

    if x not in X:
        X[x] = 0
    else:
        X[x] += 1
    
    if y not in Y:
        Y[y] = 0
    else:
        Y[y] += 1

triangles = 0
for i in range(n):
    triangles += X[xs[i]] * Y[ys[i]]
    

print(triangles)



