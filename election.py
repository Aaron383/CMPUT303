"""
  BEGIN-HEADER
  
  Name: Aaron Boyd
  
  Student-ID: 1666697

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permidtted to get help with general concepts about algorithms
  and problem solving, but you are not permidtted to hunt down solutions to
  these particular problems!

  <List Resources Here> The binomial coefficient function came from https://www.geeksforgeeks.org/binomial-coefficient-dp-9/


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

def calculate_probability(n, v1, v2):
    if v1 > n // 2:
        return 101
    
    m = n - v1 - v2
    ans = 0
    
    for i in range(n // 2 + 1 - v1, m + 1):
        ans += binomialCoef(m, i) / 2 ** m
    
    return ans * 100


# came from https://www.geeksforgeeks.org/binomial-coefficient-dp-9/
###################################################
def binomialCoef(n, k):
 
    # Calculate value of Binomial
    # Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
 
            # Calculate value using
            # previously stored values
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
 
    return C[n][k]
####################################################


T = int(input())

C = []
for i in range(51):
    C.append([0]*51)

for test in range(T):
    line = sys.stdin.readline()
    line = line[:len(line) - 1].split()
    n = int(line[0])
    v1 = int(line[1])
    v2 = int(line[2])
    w = int(line[3])



    probability = calculate_probability(n, v1, v2)

    if v1 > n // 2:
        print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
    elif v2 >= (n + 1) // 2:
        print("RECOUNT!")
    else:

        if probability > w:
            print('GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!')
        elif v1 + n - (v1 + v2) < v2:
            print('RECOUNT!')
        else:
            print('PATIENCE, EVERYONE!')
