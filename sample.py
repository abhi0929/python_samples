# def fun(*a):
#     print(a)
#     print(*a)
# fun (10,20,30,40,60)
# def fun3(a,b,c,d):
#     print(a,b,c,d)
# def fun2(**b):
#     print(b)
#     fun3(**b) 
# fun2(a=75,b=30,c=40,d=70)
# def fun5(*a,**b):
#     print(a,b,sep="\n")
# fun5(10,7,a=30,75,b=50)
# def print(*args,**kwargs,sep=" ",end="\n",file=none,flush=false)
# def fun6(*a):
#     print(sum(a))
# fun6(1,7,8,25,30,60,70)
# def fun7(*a):
#     i=0;s=0;
#     while i<len(a):
#         if a[i]%2==0:
#             s=s+a[i]
#         i+=1
#     print(s)
# fun7(1,7,8,25,30,60,70)
def fun(*a):
    i=0
    s=0
    while i<len(a):
        if i%2==0:
            s+=a[i]
        i+=1
    return s
print(fun(1,2,3,4,5,7,7,8,8,10))

def fun1(*a):
    print(sum(a[1::2]))
fun1(1,2,3,4,5,7,7,8,8,10)