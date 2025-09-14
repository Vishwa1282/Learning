def f1(l1):
    m1 = l1[0]
    for i in l1:
        if i<m1:
            m1 = i
    return m1
def f2(l1):
    m2 = l1[0]
    for i in l1:
        if i>m2:
            m2= i
    return m2
def f3(l1):
    s = 0
    for i in l1:
        s+=i
    return s
l1 = [10,20,30,40,50]
print(f1(l1))
print(f2(l1))
print(f3(l1))
