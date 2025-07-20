#Conjuntos em Python

a = {1,3,4,5}
b = {2,3,5,6}
c = a.union(b)
d = b.intersection(a)
e = a - b

print("A = ",a)
print("B = ",b)
print("C = ",c)
print("D = ",d)
print("E = ",e)