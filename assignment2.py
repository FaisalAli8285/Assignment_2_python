# Question 01: Write a program that asks the user to enter a string. The program should be in a Python file *.py. 
# The program should then print the following:\
# (a) The total number of characters in the string
# (b) The string repeated 10 times
# (c) The first character of the string
# (d) The first three characters of the string
# (e) The last three characters of the string
# (f) The string backwards
# (g) The seventh character of the string 
# (h) The string with its first and last characters removed
# (i) The string in all uppercase
# (j) The string with every “a” replaced with an “e”
# (k) The string with every letter replaced by a “space
# aaaaaaaaaaaaaaaaaaa
userInputString = input("Enter a String : ")
print("Output for part a ")
print(len(userInputString))
# bbbbbbbbbbbbbbbbbbb
print("Output for part b ")
repeatedString = (userInputString + '\n') * 10
print(repeatedString)
#ccccccccccccccccccc
print("Output for part c ")
print(userInputString[0])
print(userInputString[-6])
#ddddddddddddddddddd
print("Output for part d ")
print(userInputString[0:3])
print(userInputString[-6:-3])
#eeeeeeeeeeeeeeeeeee
print("Output for part e ")
print(f"last three characters {userInputString[-3:]}")
#fffffffffffffffffff
print("Output for part f ")
print(f"backward string is {userInputString[::-1]}")
#ggggggggggggggggggg
print("Output for part g ")
print(userInputString[6:7])
#hhhhhhhhhhhhhhhhhhh
print("Output for part h ")
length=len(userInputString)

print(f" string without first and last char {userInputString[1:length-1]}")
#iiiiiiiiiiiiiiiiiii
print("Output for part i ")
print(f" upper case {userInputString.upper()}")
#jjjjjjjjjjjjj
print("Output for part j ")
print(userInputString.replace("a","e"))
#kkkkkkkkkkkkkkkkkkk
print("Output for part k ")
print(userInputString.replace("a"," "))
# : A simple way to estimate the number of words in a string is to count the number of spaces in the 
# string. Write a program that asks the user for a string and returns an estimate of how many words are in the
# string
userInputString = input("Enter a String : ")
spaceCount=userInputString.count(' ')
print(f"total spaces {spaceCount}")
length1=len(userInputString)
totalwords=length1-spaceCount
print(f"legth of string {length1}")
print(f"totalwords{totalwords}")
# Question 03: Write a program that asks the user for their name and how many times to print it. The program
# should print out the user’s name the specified number of times.
# take input from user
userName=input("Enter your name: ")
# take integer how many times user want to repeat the name
repetionNum=int(input("Enter number of times you want to repeat: "))
# multiplication process
repeatedName=(userName + "\n")*repetionNum
print(f"your good name is :{repeatedName} ")
# Question 04: Create a program to calculate and print the following operations on a list of ten numbers: the
# mean, median, mode and standard deviation of the numbers.
# list of ten numbers
numbers = [2, 5, 9, 3, 5, 7, 4, 5, 6, 8]

# Calculate the mean
mean = sum(numbers) / len(numbers)

# Calculate the median
sorted_numbers = sorted(numbers)
n = len(numbers)
if n % 2 == 0:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
else:
    median = sorted_numbers[n // 2]

# Calculate the mode
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
mode = max(frequency, key=frequency.get)

# Calculate the standard deviation
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
std_dev = variance ** 0.5

# Printing the results
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std_dev)


# Question 05: Write a program that asks the user for a weight in kilograms and converts it to pounds. 
#2.2 pounds in a kilogram
weight=int(input("your wight in kg :"))
# conversion process
weightinPounds=2.2*weight
print(f"{weight} kg is equals to {weightinPounds}lb")
print(f"your weight in pound is {weightinPounds:.2f}")
# Q 6
# Function to convert 12-hour time format to 24-hour time
def convert_to_24_hour(time_str):
    # Extract the hour, minute, and period (am/pm)
    hour = int(time_str[:time_str.find(":")])
    minute = int(time_str[time_str.find(":") + 1:time_str.find(":") + 3])
    period = time_str[-2:].lower()
    
    # Convert hour based on am/pm
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    return hour, minute

# Function to convert 24-hour time back to 12-hour format
def convert_to_12_hour(hour, minute):
    period = "am" if hour < 12 else "pm"
    hour = hour % 12
    if hour == 0:
        hour = 12
    return f"{hour}:{minute:02d}{period}"

# Time zone offsets relative to Eastern Time (ET)
time_zone_offsets = {
    "eastern": 0,
    "central": -1,
    "mountain": -2,
    "pacific": -3
}

# Main function to convert time between time zones
def convert_time(time, from_zone, to_zone):
    # Convert input time to 24-hour format
    hour, minute = convert_to_24_hour(time)
    
    # Calculate the time difference between zones
    from_offset = time_zone_offsets[from_zone.lower()]
    to_offset = time_zone_offsets[to_zone.lower()]
    hour_difference = to_offset - from_offset
    
    # Adjust the hour based on the time zone difference
    new_hour = (hour + hour_difference) % 24
    
    # Convert back to 12-hour format for display
    return convert_to_12_hour(new_hour, minute)

# User input
time = input("Enter the time (e.g., 3:48pm or 11:26am): ").strip()
from_zone = input("Enter the first time zone (Eastern, Central, Mountain, Pacific): ").strip().lower()
to_zone = input("Enter the second time zone (Eastern, Central, Mountain, Pacific): ").strip().lower()

# Convert and display the time in the new time zone
converted_time = convert_time(time, from_zone, to_zone)
print(f"The time in {to_zone.capitalize()} Time is: {converted_time}")

# Q no 7
# Take positive integer input from the user
number = int(input("Enter a positive integer to calculate its factorial: "))

# Check if the number is positive
if number < 0:
    print("Please enter a positive integer.")
else:
    # Call the function and print the factorial result
    factorial = calculate_factorial(number)
    print(f"The factorial of {number} is {factorial}")

# Q no 8
# Ask the user for the number of Fibonacci numbers to print
num_terms = int(input("How many Fibonacci numbers would you like to print? "))

# Starting values for the first two Fibonacci numbers
a, b = 1, 1

# Print the Fibonacci sequence
print("Fibonacci Sequence:")

for _ in range(num_terms):
    print(a, end=" ")  # Print the current number
    a, b = b, a + b    # Update the values of 'a' and 'b' for the next terms
# Q NO 9
# Ask the user for the height of the diamond
height = int(input("Enter the height of the diamond: "))

# Print the top half of the diamond (including the middle line)
for i in range(height):
    # Print spaces for alignment
    print(" " * (height - i - 1), end="")
    # Print stars for the diamond shape
    print("*" * (2 * i + 1))

# Print the bottom half of the diamond
for i in range(height - 2, -1, -1):
    # Print spaces for alignment
    print(" " * (height - i - 1), end="")
    # Print stars for the diamond shape
    print("*" * (2 * i + 1))

 





