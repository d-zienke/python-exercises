"""
Task 7:

Get characters from the keyboard until the x character is entered. 
How many characters were typed?
"""

text = ""

while (user_input := input("Write something. Type 'x' to exit. ")) != "x":
    text += user_input
    print(f"You have entered {text.__len__()} characters so far")
    
print(f"In total, you have entered {text.__len__()} characters.")