def great(a,b):
    if a>b:
        return a
    else:
        return b
print(great(75,77))


def fun(*args):
    return sum(args)
x=fun(1,2,3,4,5,6,7,8,9)
if x%2==0:
    print("even")
else:
    print("odd")
print(fun(1,2,3,4,5,6,7,8,9))

def fun(x,y):
    print(x+y)
z=fun
print(z(10,45))
k=z(70,80)
print(k)


a=10
k=f"a: {a}"
print(k)
a=30
print(k)

l=[1,2,3,4,5,6,7,8,9,10]
print(l[2:7])
print(l[2:7:2])

