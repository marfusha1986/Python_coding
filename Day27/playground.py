def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum = sum + n
    return (sum)


print(add(3,5,4,6,1,2))
