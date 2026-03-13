my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))
my_set.add(6)
print(my_set)
my_set.remove(6)
print(my_set)
my_set.update([7, 8, 9])
print(my_set)

set2 = set([1,2,3,4,1,2,3])
print(set2)

set4 = set("welcome")
print(set4)

for s in set4:
    print(s)

set5 = set([1, 2, 3, 4, 5])
my_set = list(set5)
print(my_set)