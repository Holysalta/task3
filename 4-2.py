a=int(input())
alist=[]
alist.append(a)
cnt=0
for i in alist:
    while alist[i]!=alist[i+1]:
        cnt += 1
if cnt == 7 or cnt >7:
    print('NO')
else:
    print('YES')
