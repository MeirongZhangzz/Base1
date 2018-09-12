def test1():
    i = 0
    while i<5:
        if i == 0:
            temp =yield i
        else:
            yield i
        print(temp)
        i+=1