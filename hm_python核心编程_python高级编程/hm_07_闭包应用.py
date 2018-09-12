def dtest(a,b):

    def dtest_in(x):
        print(a*x+b)

    return dtest_in

line1 = dtest(1,1)
line1(0)

line2 = dtest(10,4)
line2(0)
