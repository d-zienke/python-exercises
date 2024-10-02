"""
Exercise 4.

You have this expression: (((a1+a2)*a3)-a4)/a5 (elements a1 through a5 are of float type).
Get each of the variables a1 through a5 from the keyboard, calculate the value of the expression and display the result. 
Pay attention to the value of the variable a5. In case its value is equal to 0, do not perform the action, but inform about it.
"""

prompt = "Enter a number for variable a"
equation = "(((a1+a2)*a3)-a4)/a5"
i = 1
nums = []

while i <= 5:
    try:
        nums.append(float(input(f"{prompt}{i}: ")))
        i+=1
    except:
        print("The value you entered is not a number")

a1 = nums[0]
a2 = nums[1]
a3 = nums[2]
a4 = nums[3]
a5 = nums[4]

if a5 > 0:
    result = (((a1+a2)*a3)-a4)/a5
    print(f"result: {result}")
else:
    raise ZeroDivisionError("variable a5 is 0")