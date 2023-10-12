numbers = []
for i in input().split():
    numbers.append(int(i))
min_number = sum(numbers) - max(numbers)
max_number = sum(numbers) - min(numbers)
print(min_number, max_number)