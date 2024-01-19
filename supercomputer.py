"""
  BEGIN-HEADER
  
  Name: Aaron Boyd
  
  Student-ID: 1666697

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permidtted to get help with general concepts about algorithms
  and problem solving, but you are not permidtted to hunt down solutions to
  these particular problems!

  <List Resources Here> code for the tree came from https://medium.com/@badapplesweetie/segment-trees-range-sum-queries-in-python-b2c52b24a77c


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

###############################################################
# this block came from https://medium.com/@badapplesweetie/segment-trees-range-sum-queries-in-python-b2c52b24a77c
class SegmentTree():

    def __init__(self, array):
        # first pad array to nearest 2^k
        # https://stackoverflow.com/questions/466204/rounding-up-to-next-power-of-2
        n = len(array) - 1

        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16

        n += 1

        self.arr_len = n

        tree = [0] * (n-1) + array + [0] * (n - len(array))
        # build binary tree
        for i in range(n-2, -1, -1):
            tree[i] = sum(tree[i*2 + 1: i*2 + 3])

        self.tree = tree

    def get_sum(self, l, r):
        # get leaf with value 'l'
        l += self.arr_len - 1
        # get leaf with value 'r'
        r += self.arr_len - 2

        sum = 0

        while (l <= r):

            if ((l % 2) == 0):
                # it means l is a right child
                sum += self.tree[l]

                # move l to right by 1, so it becomes a left child and find its parent
                l = (l + 1 - 1) // 2
            else:
                # when l is a left child, when just find its parent
                l = (l - 1) // 2

            if ((r % 2) == 1):
                # it means r is a left chid
                sum += self.tree[r]

                # move r to left by 1, so it becomes a right child and find its parent
                r = (r - 1 - 2) // 2
            else:
                # when r is a right child
                r = (r - 2) // 2

        return sum

    def update(self, i):


        node = self.arr_len - 1 + i

        if self.tree[node] == 0:
            value = 1
        else:
            value = 0

        self.tree[node] = value

        while node > 0:
            # find parent node
            node = (node - 1) // 2

            left_child = node * 2 + 1
            right_child = node * 2 + 2

            self.tree[node] = self.tree[left_child] + self.tree[right_child]
  
######################################################## 







n, k = map(int, input().split())
tree = [0] * (2 * n+1)

tree = SegmentTree(tree)

for x in range(k):
    q = sys.stdin.readline()
    q = q[:len(q) - 1].split()

    cmd = q[0]

    if cmd == 'F':
        index = int(q[1])
        tree.update(index)
    else:
        l = int(q[1])
        r = int(q[2])
        print(tree.get_sum(l, r))
    