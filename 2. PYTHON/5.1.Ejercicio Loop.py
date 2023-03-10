# Exercise: Use control flow and loops to solve a problem
# Introduction
# In this exercise, you will practice control flow with loops to solve problems. You will be given a list of integers 
# and you will have to add some code to find a specific number in a list and return it. 

# Instructions

from itertools import count


num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# 1.   Under the num_list create a new for loop and print out each value on the list in sequential order.

# for i in num_list:
 
#     print(i)

# 2.  Inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only 
# numbers that meet that condition

# for s in num_list:
#     if s > 45:
#         print(s)


# 3.  Change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”.

# for s in num_list:
#     if s < 45:
#         print(s)

# 4.  Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for 
# number 36 and print out the following: ‘Number found at position: ‘, index number


# for i, x in enumerate (num_list):

#     if x == 36:
#         print("Number found at position:", i )
           
         

# 5.  Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.

# 6.  Inside the for loop increment the counter by 1.

# 7.  Add a print statement outside the for loop to print the value of the count variable..


# count = 0

# for i, x in enumerate (num_list):
#     count +=  1
#     if x == 36:
#         print("Number found at position:", i )
        
# print(count)  

# 8.  Finally, add a break statement directly after the print statement inside the if condition for finding the numb

# count = 0

# for i, x in enumerate (num_list):
#     count +=  1
#     if x == 36:
#         print("Number found at position:", i )
#         break
# print(count)



