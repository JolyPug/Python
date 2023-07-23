# Задача 14: 
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

def powers_of_two(N):
    k = 0
    result = []
    power_of_two = 1

    while power_of_two <= N:
        result.append(power_of_two)
        k += 1
        power_of_two = 2 ** k

    return result

N = int(input("Введите число N: "))
powers = powers_of_two(N)
print("Целые степени двойки, не превосходящие", N, ":", powers)
