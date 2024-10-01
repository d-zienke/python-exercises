"""
Zadanie 1. [2:1,1] <abc> {~}

Pobierz z klawiatury trzy nieujemne liczby całkowite. Jeżeli któraś jest ujemna, powtórz
pobieranie. Następnie znajdź największą z nich [1]. Wyświetl sumę pozostałych
liczb tyle razy, ile wynosi wartość największej liczby [1].
"""

dest_count = 3
prompt = f"Wprowadź {dest_count} nieujemne liczby całkowite"
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
print(f"Największa liczba: {max_num}")
print(f"Suma liczb: {nums_sum}")

for i in range(max_num):
    print(nums_sum)