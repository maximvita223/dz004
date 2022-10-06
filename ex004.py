# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
import random
k = int(input())
s = []
for i in range(0,k):
    s.append(random.randint(1,10))
print(s)

data = open('file.txt','w')
for i in range(len(s)):
    if i<len(s)and k>1:
        data.write(f'{s[i]}x^{k} + ')
        k-=1
    elif k==1:
        data.write(f'{s[i]}x')  
data.write(' = 0')

