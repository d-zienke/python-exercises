"""
Exercise 1.

Get three non-negative integers from the keyboard. 
If any of them are negative, get another one. 
Then find the largest of them. 
Display the sum of the other numbers as many times as the value of the largest number.
"""

dest_count = 3
prompt = f"Enter {dest_count} non-negative integers"
counter = 1
numbers = []

while counter <= dest_count:
    user_input = input(f"{prompt} ({counter} z {dest_count}): ")
    try:
        user_input_int = int(user_input)
        if user_input_int >= 0:
            numbers.append(user_input_int)
            counter += 1
    except:
        continue

max_num = max(numbers)
nums_sum = sum(numbers)
print(f"The highest number: {max_num}")
# print(f"Sum of numbers: {nums_sum}")

for i in range(max_num):
    print(f"Sum: {nums_sum}")