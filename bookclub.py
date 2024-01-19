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

def find_augmenting_path(current_node, adjacency_list, left_matches, right_matches, visited):
    if visited[current_node]:
        return False
    visited[current_node] = True

    for neighbor in adjacency_list[current_node]:
        if right_matches[neighbor] == -1 or find_augmenting_path(right_matches[neighbor], adjacency_list, left_matches, right_matches, visited):
            left_matches[current_node] = neighbor
            right_matches[neighbor] = current_node
            return True

    return False

def max_bipartite_matching(adjacency_list, num_left_nodes, num_right_nodes):
    left_matches = [-1] * num_left_nodes
    right_matches = [-1] * num_right_nodes
    visited = [0] * num_left_nodes

    while True:
        found_augmenting_path = False
        visited = [0] * num_left_nodes

        for i in range(num_left_nodes):
            if left_matches[i] == -1:
                found_augmenting_path |= find_augmenting_path(i, adjacency_list, left_matches, right_matches, visited)

        if not found_augmenting_path:
            break

    max_matching_count = sum(left_matches[i] != -1 for i in range(num_left_nodes))
    return max_matching_count

line = sys.stdin.readline()
line = line[:len(line) - 1].split()
n = int(line[0])
m = int(line[1])

adjacency_list = []
for _ in range(n):
    adjacency_list.append([])


for _ in range(m):
    line = sys.stdin.readline()
    line = line[:len(line) - 1].split()
    a = int(line[0])
    b = int(line[1])
    adjacency_list[a].append(b)

if max_bipartite_matching(adjacency_list, n, n) == n:
    print("YES")
else:
    print("NO")
 