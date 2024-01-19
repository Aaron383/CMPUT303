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

line = sys.stdin.readline()
line = line[:len(line) - 1].split()
p1 = (int(line[0]), int(line[1]))

line = sys.stdin.readline()
line = line[:len(line) - 1].split()
p2 = (int(line[0]), int(line[1]))

line = sys.stdin.readline()
line = line[:len(line) - 1].split()
p3 = (int(line[0]), int(line[1]))

line = sys.stdin.readline()
line = line[:len(line) - 1].split()
xv = int(line[0])
yv = int(line[1])
r = int(line[2])

x = 0
y = 1

# speed
a = xv**2 + yv**2

# for partical 2
b = 2*(xv*(p1[x]-p2[x])+yv*(p1[y]-p2[y]))
c = (p1[x]-p2[x])**2+(p1[y]-p2[y])**2-4*r*r
d = b*b-4*a*c

# for partical 3
b2 = 2*(xv*(p1[x]-p3[x])+yv*(p1[y]-p3[y]))
c2 = (p1[x]-p3[x])**2+(p1[y]-p3[y])**2-4*r*r
d2 = b2*b2-4*a*c2

# if partical 1 does not hit either partical
if d < 0 and d2 < 0:
    print(5)

# if it hit particle 3
elif d < 0: 
    t = (-b2-d2**0.5)/(2*a)
    if t < 0: 
        print(5)
    vx, vy = p3[x]-p1[x]-xv*t, p3[y]-p1[y]-yv*t 
    sx, sy, px, py = p3[x], p3[y], p2[x], p2[y];
    v = [2, 4]

# if it will hit partival 2
elif d2 < 0: 
    t = (-b-d**0.5)/(2*a)
    if t < 0: 
        print(5)
    vx, vy = p2[x]-p1[x]-xv*t, p2[y]-p1[y]-yv*t
    sx, sy, px, py = p2[x], p2[y], p3[x], p3[y]
    v = [1, 3]

# on path to hit both  
else: 
    t1 = (-b-d**0.5)/(2*a)
    t2 = (-b2-d2**0.5)/(2*a)
    if t1 < t2 or t2 < 0: 
        vx, vy = p2[x]-p1[x]-xv*t1, p2[y]-p1[y]-yv*t1
        sx, sy, px, py = p2[x], p2[y], p3[x], p3[y]
        v = [1, 3]
    elif t1 > t2 or t1 < 0: 
        vx, vy = p3[x]-p1[x]-xv*t2, p3[y]-p1[y]-yv*t2
        sx, sy, px, py = p3[x], p3[y], p2[x], p2[y]
        v = [2, 4]
    else: 
        print(5)


# Will (sx, sy) + t*(vx, vy) hit (px, py)?
a = vx**2 + vy**2
b = 2*(vx*(sx-px)+vy*(sy-py))
c = (sx-px)**2+(sy-py)**2-4*r**2
d = b**2-4*a*c


print(v[d<0 or d**0.5<b])