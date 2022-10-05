# Вычислить число π c заданной точностью d

import math
from decimal import Decimal, ROUND_FLOOR



n = input('Введите какую точность нужно (Пример - 0.01) = ')
number = Decimal(math.pi)
number = (number.quantize(Decimal(f"{n}"),ROUND_FLOOR))
print(number)