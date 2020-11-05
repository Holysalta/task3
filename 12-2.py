size = int(input())
file_name = str(input())
location = 0
cnt = 0
if file_name[2] != "x":
    print(0)
    exit(0)
else:
    for i in range(size):
        if file_name[i] != "x":
            location = i
            break
if location == 0:
    print(size - 2)
else:
    for i in range(0, location):
        if file_name[i] == "x":
            cnt = cnt + 1
    print(cnt-2)




