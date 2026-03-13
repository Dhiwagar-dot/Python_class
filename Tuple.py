empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

tuple1 = (1, 2, 3,'hello')
print(tuple1)
tuple2 = (4, 5, 6,'world')
print(tuple2)
# Concatenation
tuple3 = tuple1 + tuple2
print(tuple3)

tuple3 = (12)
print(tuple3)

tuple4 = (10,20,30,40,50)
print(tuple4[0])  # 10
print(tuple4[-2])  # 40
print(tuple4[1:4])  # (20, 30, 40)
print(len(tuple4))  # 5
print(20 in tuple4)  # True
print(100 in tuple4)  # False
print(max(tuple4))  # 50
print(min(tuple4))  # 10
print(tuple4.count(20))  # 1
for s in tuple4:
    print(s)