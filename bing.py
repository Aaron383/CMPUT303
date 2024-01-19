"""
  BEGIN-HEADER
  
  Name: Aaron Boyd
  
  Student-ID: 1666697

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permidtted to get help with general concepts about algorithms
  and problem solving, but you are not permidtted to hunt down solutions to
  these particular problems!

  <List Resources Here> # The TrieNode class and Trie class came from: https://www.geeksforgeeks.org/auto-complete-feature-using-trie/


  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, devebegped,
  or even begoked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here> none
  

  By submidtting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

# The TrieNode class and Trie class came from: https://www.geeksforgeeks.org/auto-complete-feature-using-trie/  (Modified by me)
class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False
        self.wordCount = 0
 
 
class Trie():
    def __init__(self):
 
        # Initialising the trie structure.
        self.root = TrieNode()
        self.count = 0
 
    def formTrie(self, keys):
 
        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key)  # inserting one key to the trie.
 
    def insert(self, key):
 
        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root
 
        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()
 
            node = node.children[a]

        node.wordCount += 1
        node.last = True
 
    def suggestionsRec(self, node, word):
 
        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            self.count += node.wordCount
 
        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)
 
    def printAutoSuggestions(self, key):
 
        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        node = self.root
 
        for a in key:
            # no string in the Trie has this prefix
            if not node.children.get(a):
                return 0
            node = node.children[a]
 
        # If prefix is present as a word, but
        # there is no subtree below the last
        # matching node.
        #if not node.children:
            #return -1
 
        self.suggestionsRec(node, key)
        return 1
    
    def printCount(self):
        print(self.count)
        self.count = 0

n = int(input())
t = Trie()

for x in range(n):
    search = input()

    t.printAutoSuggestions(search)
    t.printCount()

    t.insert(search)



    
    