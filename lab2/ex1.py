def rectangle_area(a, b):
    """
    Функція для обчислення площі прямокутника
    Параметри:
        a (float): довжина сторони a
        b (float): довжина сторони b
    Повертає:
        float: площа прямокутника
    """
    return a * b

# Цикл для введення сторін та обчислення площ трьох прямокутників
for i in range(3):
    a = float(input(f"Введіть довжину сторони a {i+1}-го прямокутника: "))
    b = float(input(f"Введіть довжину сторони b {i+1}-го прямокутника: "))
    area = rectangle_area(a, b)
    print(f"Площа {i+1}-го прямокутника: {area}")