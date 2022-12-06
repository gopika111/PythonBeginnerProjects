values = input('Enter the number in a single line seperated by space :')
print(values.split(" "))
result = map(int, values.split(" "))
print(list(result))

list1 = ['|' for i in range(3)]
for val in list1:
    print(val)
    