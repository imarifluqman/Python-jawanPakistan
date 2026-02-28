my_list = [10, 20, 30, 40, 50]

print("Length of list is:", len(my_list))


numbers = [1, 2, 3, 4, 5]

total = sum(numbers)
print("Sum is:", total)

numbers = [1, 2, 3, 4, 5]

total = 0
for num in numbers:
    total += num

print("Sum is:", total)

numbers = [10, 25, 5, 80, 40]

largest = max(numbers)
print("Largest number is:", largest)

numbers = [10, 25, 5, 80, 40]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for num in a:
    if num < 5:
        print(num)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

result = [num for num in a if num < 5]
print(result)



