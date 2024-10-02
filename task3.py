"""
Task 3:

Get an integer from the keyboard and check if it is divisible: 
by 3 and by 5; 
by 3, but not by 5; 
by 5, but not by 3; 
neither by 3 nor by 5. 
Display the correct answer on the screen.
"""

user_input = input("Enter an integer: ")
try:
    user_input_int = int(user_input)
except ValueError as e:
    print(e)
    raise

test1 = user_input_int % 3 == 0 and user_input_int % 5 == 0
test2 = user_input_int % 3 == 0 and user_input_int % 5 != 0
test3 = user_input_int % 3 != 0 and user_input_int % 5 == 0
test4 = user_input_int % 3 != 0 and user_input_int % 5 != 0

if test1:
    print(f"The number {user_input_int} is divisable by 3 and by 5")
if test2:
    print(f"The number {user_input_int} is divisable by 3, but not by 5")
if test3:
    print(f"The number {user_input_int} is divisable by 5, but not by 3")
if test4:
    print(f"The number {user_input_int} is divisable neither by 3 nor by 5")
