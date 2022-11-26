list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max = 0
h = 0
for k, i in enumerate(list_numbers):
    if i >= max:
        max = i
        h = k
list_numbers[h], list_numbers[-1] = list_numbers[-1], max
print(list_numbers)

# Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
