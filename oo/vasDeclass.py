class A:
    num = 123
    


a1 = A()
a2 = A()

a2.num = 312

print(a1.num)
print(a2.num)
print(A.num)

print(a2.__dict__)
