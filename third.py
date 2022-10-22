#Задайте последовательность чисел. Напишите программу, 
# которая выведет список 
# неповторяющихся элементов исходной последовательности.

first_array = list(map(int, input(' posledovadetlnost = \n').split()))
print(first_array)

second_array = []

for i in first_array:
    if i not in second_array:
        second_array.append(i)
    
    
print(second_array)