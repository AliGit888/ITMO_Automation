a = [5, 10, 15, 29, 25, 30, 35, 40]
print("a[2] = ", a[2])
print("a[0:3] = ", a[0:3])

b = [11, 12, 13]
b[2] = 4 #изменение элемента
print(b)

test_list = ['один','два','три']
for elem in test_list: #цикл
    print(elem)

print(len(test_list))
test_list.append('четыре') #добавить значение в конце
print(test_list)