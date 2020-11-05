def upperfirst(x):
    i = 1
    return x[:i].upper() + x[i:]

x = raw_input(str())

y = upperfirst(x)

print(y)