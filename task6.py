"""
Task 6:

Get the character from the keyboard. Check if it's a vowel, consonant, or digit. 
Inform what kind of character it is. Include only lowercase letters of the English alphabet and numbers.
"""

import re

regex_pattern_vowel = r"[euioa]"
regex_pattern_consonant = r"[qwrtypsdfghjklzxcvbnm]"
regex_pattern_number = r"[0-9]"

user_input = input("Enter a character: ")
user_input = user_input[0].lower()

is_vowel = re.match(regex_pattern_vowel,user_input)
is_consonant = re.match(regex_pattern_consonant,user_input)
is_number = re.match(regex_pattern_number,user_input)

if is_vowel:
    print(f"{user_input} is a vowel")
elif is_consonant:
    print(f"{user_input} is a consonant")
elif is_number:
    print(f"{user_input} is a number")
else:
    print(f"{user_input} is unknown")
