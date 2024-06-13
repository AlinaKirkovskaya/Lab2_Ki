import math

def polygon_area(X, Y, Z, T):
    """
    Функція для обчислення площі чотирикутника
    Параметри:
        X (float): довжина сторони X
        Y (float): довжина сторони Y
        Z (float): довжина сторони Z
        T (float): довжина сторони T
    Повертає:
        float: площа чотирикутника
    """
    diagonal1 = math.sqrt(X**2 + Y**2)
    diagonal2 = math.sqrt(Z**2 + T**2)

    area = 0.5 * diagonal1 * diagonal2

    return area

X = float(input("Введіть довжину сторони X: "))
Y = float(input("Введіть довжину сторони Y: "))
Z = float(input("Введіть довжину сторони Z: "))
T = float(input("Введіть довжину сторони T: "))

area = polygon_area(X, Y, Z, T)

print(f"Площа чотирикутника: {area}")