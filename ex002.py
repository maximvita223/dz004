# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число - '))
spi = []
i = n
while n!=1:
    for j in range(2,100):
        for k in range(2,100):
            if not n%j:
                n = n//j
                spi.append(j)
if spi[0]==i:
    spi.append(1)         
print(spi)
