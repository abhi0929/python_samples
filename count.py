# def fun(x,y):
#     print(x,y)
#     return x+y
# def fun2(a,b):
#     c=fun(a,b)
#     print(c*c)
# fun2(10,20)

# def fun3(a,b):
#     print(a,b)
# def fun4(x,y,z):
#     x(y,z)
# fun4(fun,10,50)

# def fun():
#     def fun2():
#         print("hello")
#     fun2()
# fun()

# def fun():
#     x=50
#     y=50
#     z=x+y
#     def fun2():
#         print("hii")
#     return fun2
# f=fun()
# f()
#with out using map function or any lamda
l=[66,67,68,69,70]
list_i=[]
for i in range (len(l)):
    q=l[i]+4
    list_i.append(q)
    print(chr(q))

