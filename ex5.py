"""
Exercise 5.

Get five integers from the keyboard and display how many of them were even and how many were odd.
"""

nums = []
i = 1

while nums.__len__() < 5:
    try:
        nums.append(int(input(f"Enter an integer ({i} of 5): ")))
        i+=1
    except:
        print("The value you entered is not an integer")


even_nums = [num for num in nums if num%2==0]

even_nums_count = even_nums.__len__()

print(f"{even_nums_count} numbers are even and {5-even_nums_count} are odd")