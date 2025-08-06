#creating an empty list

my_list = []

#apending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#inserting the value 15
my_list.insert(1, 15)

print(my_list)

#extending my_lis with another list
my_list.extend([50, 60, 70])

print(my_list)


#removing the last element
my_list.pop()

print(my_list)

#sorting in ascending order

my_list.sort()

print(my_list)

#finding index of the value 30

index_30 = my_list.index(30)

print(index_30)
