"""
  BEGIN-HEADER
  
  Name: Aaron Boyd
  
  Student-ID: 1666697

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permidtted to get help with general concepts about algorithms
  and problem solving, but you are not permidtted to hunt down solutions to
  these particular problems!

  <List Resources Here> Bipartite matching algorithm came from: https://www.geeksforgeeks.org/maximum-bipartite-matching/


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


# Bipartite matching algorithm came from: https://www.geeksforgeeks.org/maximum-bipartite-matching/
####################################################################
class GFG:
    def __init__(self,graph):
         
        # residual graph
        self.graph = graph 
        self.ppl = len(graph)
        self.jobs = len(graph[0])
 
    # A DFS based recursive function
    # that returns true if a matching 
    # for vertex u is possible
    def bpm(self, u, matchR, seen):
 
        # Try every job one by one
        for v in range(self.jobs):
 
            # If applicant u is interested 
            # in job v and v is not seen
            if self.graph[u][v] and seen[v] == False:
                 
                # Mark v as visited
                seen[v] = True
 
                '''If job 'v' is not assigned to
                   an applicant OR previously assigned 
                   applicant for job v (which is matchR[v]) 
                   has an alternate job available. 
                   Since v is marked as visited in the 
                   above line, matchR[v]  in the following
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v], 
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False
 
    # Returns maximum number of matching 
    def maxBPM(self):
        '''An array to keep track of the 
           applicants assigned to jobs. 
           The value of matchR[i] is the 
           applicant number assigned to job i, 
           the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs
         
        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):
             
            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs
             
            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1
        return result
################################################################################



def findDistance(p1, p2):
    x = (p1[0]-p2[0])**2
    y = (p1[1]-p2[1])**2
    return math.sqrt(x+y)


def checkAnswer(N, B, R, distance, d):

    graph = []
    for i in range(R):
        graph.append([0]*B)

    for i in range(R):
        for j in range(B):
            if distance[i][j] < d:
                graph[i][j] = 1
    
    #return if the max matching is more than N
    g = GFG(graph)
    #print(g.maxBPM())
    return R + B - g.maxBPM() >= N


line = sys.stdin.readline()
line = line[:len(line) - 1].split()
N = int(line[0])
B = int(line[1])
R = int(line[2])

blues = []
reds = []

for egg in range(B):
    line = sys.stdin.readline()
    line = line[:len(line) - 1].split()
    line = tuple(map(float, line))
    blues.append(line)

for egg in range(R):
    line = sys.stdin.readline()
    line = line[:len(line) - 1].split()
    line = tuple(map(float, line))
    reds.append(line)


distance = []

for i in range(R):
    row = []
    for j in range(B):
        d = findDistance(blues[j], reds[i])
        row.append(d)
    distance.append(row)

hi = 10000000000
lo = 0
mid = (hi+lo)//2



while hi-lo > 0.0000000001:
    mid = (hi+lo)/2
    d = mid

    if checkAnswer(N, B, R, distance, d):
        lo = mid
    else:
        hi = mid

print(f"{d:.8f}")
