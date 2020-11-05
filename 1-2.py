def result(a):
    vowels=('a','e','i','o','u')
    for i in a.lower():
        if i in vowels:
            a=a.replace(i,'.')
    print(a)
b=raw_input(str())
a=b.lower()
result(a)
