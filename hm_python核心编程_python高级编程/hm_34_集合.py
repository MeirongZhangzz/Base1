a = "abcdef"
b = set(a) # 集合
A = "bdf"
B = set(A)
print(b)
print(B)
print(b&B) # 交集
print(b|B) # 并集
print(b-B) # 差集
print(b^B) # 对称差集