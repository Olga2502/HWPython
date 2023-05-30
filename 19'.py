#Дана последовательность из N целых чисел и число 
#K. Необходимо сдвинуть всю последовательность 
#(сдвиг - циклический) на K элементов вправо, K – 
#положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]

import random
lst = []
for i in range(10):
    lst.append(random.randint(1,100))
print(lst)
N = int(input('введите число '))
for i in range(N):
    a = lst.pop()
    lst.insert(0,a)
    print(lst)

a = [4, 5, 7, 3, 2, 9, 5, 89]
#a = [9, 5, 89, 4, 5, 7, 3, 2]
k = 3
b = a[-k:]
c = a[:-k]
print(b + c)