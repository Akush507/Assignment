import random

numbers = []  
for i in range(15):
    numbers.append(random.randint(1, 100)) 


list1 = numbers[0:5]
list2 = numbers[5:10]
list3 = numbers[10:15]

sum1 = sum(list1)
sum2 = sum(list2)
sum3 = sum(list3)

print("List 1:", list1, "Sum:", sum1)
print("List 2:", list2, "Sum:", sum2)
print("List 3:", list3, "Sum:", sum3)

if sum1 >= sum2 and sum1 >= sum3:
    print("List 1 has the greatest sum.")
elif sum2 >= sum1 and sum2 >= sum3:
    print("List 2 has the greatest sum.")
else:
    print("List 3 has the greatest sum.")
