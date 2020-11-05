number = int(input())
words = str(input())
ans = []
z = 0
n = 0
for i in words:
    if i == 'z':
        z = z + 1
    
    elif i == 'n':
        n = n + 1

for i in range(z):
    ans.append(0)
for i in range(n):
    ans.append(1)
for i in ans:
    print(i, end=" ")              
       

