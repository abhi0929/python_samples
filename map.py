# l=[[1,2],[3,4],[5,6]]
# k=list(map(lambda x:x+[5],l))
# print(k)
# print(l)
#
# l=[1,7,8,12,14,21,22,63,66]
# k=list(map(lambda x:x**3,l))
# print(k)
# e=list(filter(lambda x: x%4,k))
# print(e)
#
# from functools import reduce
# st=['.','j','o','i','n','(',')']
# k=reduce(lambda x,y: x+y,st,'@')
# print(k)

# from functools import reduce
# l=[1,7,6,3,8,9,11,10]
# k=reduce(lambda x,y: x if x>y else y, l)
# print(k)

# from functools import reduce
# l=[0,22,31,35,23]
# f=list(map(lambda x:(9/5*x)+32,l))
# fi=list(filter(lambda x:x%3==0,f))
# fs=reduce(lambda x,y:x+y,fi,0)
# print(fs)
