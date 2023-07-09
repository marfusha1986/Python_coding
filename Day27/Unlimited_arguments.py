def add(n1,n2):
    return n1 + n2

print(add(1,2))

def add(*args):
    for n in args:
        print(n)

add(5,3,8,9)