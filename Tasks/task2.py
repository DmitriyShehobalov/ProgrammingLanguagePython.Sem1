# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
print('Enter three-digit number:')
num = int(input())
num1 = num % 10
num2 = num//10%10
num3 = num//100
print(num1+num2+num3)
