n = int(input())
sisters = 0
for i in input().split():
    sisters += int(i)
if sisters >= n:
    print('Yes') 
else:
    print('No')