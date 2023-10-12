int(input())
numbers = []
for i in input().split():
  numbers.append(int(i))
for i in numbers:
  if numbers.count(i) == 1:
    print(i)
    break