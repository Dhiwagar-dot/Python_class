my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list) 

my_listnew = [1, 2, 4 ]
my_listnew.insert(2, 3)
print(my_listnew) 

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

new_list = list1 + list2
print(new_list)

list2 = [4, 5, 6]
list2.remove(5)
del list2[0:4]
print(list2)

# pop() – remove element using index
numbers = [10, 20, 30, 40]
numbers.pop(2)
print(numbers)

numbers = [10, 20, 30, 40]
del numbers[1]
print(numbers)  # [10, 30, 40]

numbers = [10, 20, 30]

numbers[1] = 50

print(numbers)  # [10, 50, 30]

numbers = [10, 20, 30]
numbers[1:3] = [50, 60]
print(numbers) 

print(len(numbers) - 1)  # 3   

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])  # [20, 30, 40]

# reverse()
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)

# sort()
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)


numbers = [10, 20, 30, 40]
if 20 in numbers:
    print("Found")

for num in numbers:
    print(num)

numbers = [10, 20, 30]

numbers.append(40)
numbers.remove(20)

for n in numbers:
    print(n)
    