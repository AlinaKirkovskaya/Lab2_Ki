import math

def is_inside_circle(x, y, a, b, R):
    """
    Функція для перевірки, чи лежить точка всередині кола
    Параметри:
        x (float): координата x точки
        y (float): координата y точки
        a (float): координата x центра кола
        b (float): координата y центра кола
        R (float): радіус кола
    Повертає:
        bool: True, якщо точка лежить всередині кола, інакше False
    """
    distance = math.sqrt((x - a)**2 + (y - b)**2)
    return distance <= R

a = float(input("Введіть координату a центра кола: "))
b = float(input("Введіть координату b центра кола: "))
R = float(input("Введіть радіус R кола: "))

p1 = float(input("Введіть координату x точки P: "))
p2 = float(input("Введіть координату y точки P: "))

f1 = float(input("Введіть координату x точки F: "))
f2 = f1  # Координата y такої ж як x (лежить на прямій y=x)

l1 = float(input("Введіть координату x точки L: "))
l2 = float(input("Введіть координату y точки L: "))

points_inside = 0
if is_inside_circle(p1, p2, a, b, R):
    points_inside += 1
if is_inside_circle(f1, f2, a, b, R):
    points_inside += 1
if is_inside_circle(l1, l2, a, b, R):
    points_inside += 1

print(f"\nКількість точок всередині кола: {points_inside}")