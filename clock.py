"""
  BEGIN-HEADER
  
  Name: Aaron Boyd
  
  Student-ID: 1666697

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  time formula I used came from: https://www.quora.com/What-is-the-angle-between-the-hour-hand-and-the-minute-hand-at-3-50-pm

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here> none
  

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

angle = int(input())


for hour in range(12):
    for min in range(60):
        min_angle = 60 * min
        hour_angle = 300 * hour + 5 * min


        test_angle = abs(hour_angle - min_angle)

        if min_angle < hour_angle:
            
            hour_angle = 3600 - hour_angle
            test_angle = abs(hour_angle + min_angle)

        
        if angle == test_angle:
    
            print(f"{hour:02d}:{min:02d}")
            exit()
        """
        elif angle == (3600-test_angle):
            print(test_angle)
            print(min_angle)
            print(hour_angle)
            print(f"{hour:02d}:{min:02d}")
            exit()
        """


'''
for hour in range(12):
    for min in range (60):
      
        test_angle = abs((300*hour)-(55*min))

        

        if angle == (3600-test_angle):
            print(f"{hour:02d}:{min:02d}")
            exit()
        
        elif angle == test_angle:
     
          print(f"{hour:02d}:{min:02d}")
          exit()
'''

