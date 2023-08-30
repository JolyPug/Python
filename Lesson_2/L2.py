
# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а 
# некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


def min_flips(coins):
    heads_count = 0
    tails_count = 0

    for coin in coins:
        if coin == 'H':
            heads_count += 1
        elif coin == 'T':
            tails_count += 1

    return min(heads_count, tails_count)

n = int(input("Введите количество монеток: "))
coins = input("Введите последовательность монеток (например, 'HTHTHHT'): ")

if len(coins) != n:
    print("Ошибка ввода. Количество монеток не соответствует указанному значению.")
else:
    flips_needed = min_flips(coins)
    print("Минимальное количество монет, которые нужно перевернуть:", flips_needed)


# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


def find_numbers_with_hints(S, P):
    for x in range(1, 1001):
        for y in range(1, 1001):
            if x + y == S and x * y == P:
                return x, y
    return None

S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))

result = find_numbers_with_hints(S, P)

if result:
    x, y = result
    print(f"Задуманные числа: {x} и {y}")
else:
    print("Невозможно определить задуманные числа с данными подсказками.")
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
