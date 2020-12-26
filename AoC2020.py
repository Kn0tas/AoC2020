#Solution 2 december 2020

"""
with open("aoc2dec.txt", "r") as file:  # Open aoc text file and store as "file"
    input = file.readlines()            # Read each line of "file" and store each line in list as a string in "input"

line_input = [i.split("\n")[0] for i in input] # Split "input" to get rid of \n as in "input" and store as line_input.
num_of_valid_passwords_1 = 0
num_of_valid_passwords_2 = 0

for lines in line_input:
    condition, password = lines.split(": ")                     # Split the password and condition for each line and store them
    low_and_high, letter_to_be_checked = condition.split(" ")   # Split the condition into low/high values and letter condition
    low_number, high_number = low_and_high.split("-")           # Split the low/high numbers separately
    low_int, high_int = int(low_number), int(high_number)

    if low_int <= password.count(letter_to_be_checked) <= high_int:
        num_of_valid_passwords_1 = num_of_valid_passwords_1 + 1

    if password[low_int - 1] == letter_to_be_checked and password[high_int - 1] != letter_to_be_checked:
        num_of_valid_passwords_2 = num_of_valid_passwords_2 + 1
    elif password[low_int - 1] != letter_to_be_checked and password[high_int - 1] == letter_to_be_checked:
        num_of_valid_passwords_2 = num_of_valid_passwords_2 + 1

print(num_of_valid_passwords_1)
print(num_of_valid_passwords_2)

"""
import math
#Solution 3 december 2020

with open("aoc3dec.txt", "r") as file:  # Open aoc text file and store as "file"
    input = file.readlines()            # Read each line of "file" and store each line in list as a string in "input"

line_input = [i.split("\n")[0] for i in input] # Split "input" to get rid of \n as in "input" and store as line_input.

column = 0
row = 0
tree_count = [0, 0, 0, 0, 0]
row_step = [1, 1, 1, 1, 2]
column_step = [1, 3, 5, 7, 1]
for x in range(5):
    print(x)
    for line in line_input:
        if row < len(line_input) and line_input[row][column] == "#":
            tree_count[x] = tree_count[x] + 1

        column = column + column_step[x]
        row = row + row_step[x]

        if column >= 31:
            column = column - 31
    column = 0 # Return to top left corner
    row = 0

print(tree_count)
print(math.prod(tree_count))















