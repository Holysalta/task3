word = str(raw_input())
length = len(word)
new = ""
for i in range(1,length):
    new += word[i].lower()

print(word[0].upper() + new)  