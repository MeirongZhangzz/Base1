ret = map(lambda x:x*x,[1,2,3])

for tmp in ret:
    print(tmp)

ret1 = map(lambda x,y:x+y,[1,2,3],[4,5,6])

for tmp1 in ret1:
    print(tmp1)


def f1(x,y):
    return (x,y)

l1 = [0,1,2,3,4,5,6]
l2 = ["sun","M","T","W","T","F","S"]
l3 = map(f1,l1,l2)
print(list(l3))

# filter(None,"she")
# reduce(lambda x,y:x+y,["aa","bb","cc"],"dd)