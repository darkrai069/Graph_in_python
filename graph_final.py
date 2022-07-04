print("This is a Input-Powered Graph")
print("Enter any number of inputs names and their curresponding value")

"""
 ABOUT The Program
 > each user takes up 4 collumns
 > middle users are supposed to take 6 columns
 > say "n" be the number of users to plot then there would be [ n*5+(n-2) ] no. collumns
 > r = small_list length
 > c = big_list length

"""

# Initialization
from operator import lt

# ----------- Inputting Values ----------------------
username_list = list()
value_list = list()
users_num = int(input("Enter the number of users : "))

# User input "names" and curresponding "values"
for i in range(users_num):
    print("User - ", i+1)
    print("[+] Use 3 letter abbreviation for names!!!")

    users_val = input("Enter the username : ")
    username_list.append(users_val)
    lets_read = input("Enter the values of each input : ")
    value_list.append(int(lets_read))
    print(" ")
    if i == users_num-1:
        print("[+] Username Iteration Completed !!! ")
print("username LIST entries : ", username_list)
# print(value_list)
# -----------------------------------------------------

# setting ROWs and COLLUMNs for the whole process
c = users_num*5+users_num-2
r = max(value_list)+4

# -----------------------------------------------------

"""
 > Creat a grand list-inside-list.
 > length of small lists; r = no. rows
 > Length of the BIG list; c = no. collumn.
"""


def auto_list_making(cols, rows):
    big_lst = list()
    # For loop for Big List => collumns
    for i in range(0, cols):
        small_list = list()
        # For Loop for Small List => rows
        for j in range(0, rows):
            small_list.append(" ")
        big_lst.append(small_list)
    return(big_lst)


graph_list = auto_list_making(c, r)
# -----------------------------------------------------


# Creating the Graph to Plot the Values
# Graph syntax : graph[collumn][row]
def tictactoe(field):
    for row in range(0, r):

        for collumn in range(0, c):

            if collumn != c-1:
                print(field[collumn][row], end="")

            else:
                print(field[collumn][row])


tictactoe(graph_list)
# -----------------------------------------------------


# Marking of X-axis and Y-axis ranges.
# X-AXIS
count = 1
start = r-3

for i in range(start, -1, -1):
    graph_list[0][i] = count
    count += 1
# Y-AXIS
users = users_num+1
for i in range(1, users):
    j = i-1
    user_tag = " "+username_list[j]+" "
    graph_list[i][r-1] = user_tag
# -----------------------------------------------------

# Beautification
for i in range(c):
    graph_list[i][r-2] = "-"
# -----------------------------------------------------


# Generalize the Plotting Scheme:-
"""
 > Things to Consider
 > Row and Collumn always ends at 0
 > Rows : R
 > Collumns : C
    - Location where "1" is starting.
        --> R-2
        --> You go from 'R-2' down, that many steps equal to your value.
    - 1st entry always starts at 3 and you go 5 steps up to write the 2nd entry and so on.
    - always substract one if the magnitude exceeds 10 to beautify things.
    - Inputs are in username list.

 > collumn starting is 3 and increment is 5

"""

change = start-9
c_start = 3
c_prev = c_start-1

for val in value_list:
    mag = val
    end = start-mag

    for i in range(start, end, -1):
        if i > change:
            graph_list[c_start][i] = "$"
        else:
            graph_list[c_start-1][i] = "$"
    c_start = c_start+5
# -----------------------------------------------------


tictactoe(graph_list)
