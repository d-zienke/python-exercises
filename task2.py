"""
Task 2:

Verify the integer taken from the keyboard for parity. 
Display an adequate message when it is or is not even.
"""

prompt = "Enter an integer: "

user_input = input(prompt)
try:
    user_input_num = int(user_input)
    is_even = user_input_num % 2 == 0
    if is_even:
        print(f"Number {user_input_num} is even")
    else:
        print(f"Number {user_input_num} is odd")
except:
    print("The value you entered wasn't an integer")