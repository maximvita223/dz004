# Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача - сформировать файл, содержащий сумму многочленов


data_1 = open('polynomial1.txt','r')
s = [line.split('',' ') for line in data_1]
data_2 = open('polynomial2.txt','r')
s_1 = [line.split('',' ') for line in data_2]
print(s)
print(s_1)
