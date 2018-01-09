def calc():
    x = 10
    y = 12

    def add():
        #print(x+y)
        return x + y

    def sub():
        #print(x-y)
        return x - y

    return add, sub

#print(calc())
a,b = calc()
print(a())
print(b())
