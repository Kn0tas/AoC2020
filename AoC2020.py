#Solution 2 december 2020

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









