from functools import reduce
l=[1,7,8,12,14,21,22,63,66]
# k=
# print(k)

# y =
print(list(filter(lambda x: x%2==1,list(map(lambda x:x**3,l)))))



print()
print(reduce(lambda x,y: x if x>y else y, list(filter(lambda x : x%2 == 1,list(map(lambda x : x**3,l)) ))))
