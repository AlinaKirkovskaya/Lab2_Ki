def find_divisible_numbers(n, divisors):
    """
    Функція для пошуку натуральних чисел, що не перевищують n і діляться на кожне із заданих чисел
    Параметри:
        n (int): максимальне натуральне число
        divisors (list): список чисел, на які потрібно ділитися
    Повертає:
        list: список натуральних чисел, що задовольняють умову
    """
    result = []
    for i in range(1, n+1):
        if all(i % d == 0 for d in divisors):
            result.append(i)
    return result

n = int(input("Введіть максимальне натуральне число: "))
divisors = [int(d) for d in input("Введіть числа, на які потрібно ділитися (через пробіл): ").split()]

divisible_numbers = find_divisible_numbers(n, divisors)
print(f"Натуральні числа, що діляться на {', '.join(map(str, divisors))}: {', '.join(map(str, divisible_numbers))}")