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

def find_substrings(dictionary, input_str):
    substring_positions = []

    for word in dictionary:
        start_pos = input_str.find(word)
        while start_pos != -1:
            end_pos = start_pos + len(word) - 1
            substring_positions.append((start_pos, end_pos))
            start_pos += 1
            start_pos = input_str.find(word, start_pos)

    return substring_positions

def count_non_overlapping_substrings(substring_positions):
    substring_positions.sort(key=lambda x: x[1])

    end = -1
    count = 0

    for position in substring_positions:
        if position[0] > end:
            end = position[1]
            count += 1

    return count

dictionary_words = []
word = input()
while word != "#":
    dictionary_words.append(word)
    word = input()

concatenated_string = ""
current_string = input()

while current_string != "#":
    concatenated_string += current_string
    if concatenated_string[-1] == '|':
        substrings = find_substrings(dictionary_words, concatenated_string)
        result = count_non_overlapping_substrings(substrings)
        print(result)
        concatenated_string = ""
    current_string = input()


