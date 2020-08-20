import math


def tochki(a, b, c):
    if a == 0:
        print("не квадратное")
    else:
        d = b * b - 4 * a * c
        if d < 0:
            print('нет корней')
        elif math.fabs(d) < 1e-9:
            print('имеет единственый корень')
            x = -b / (2 * a)
            print(x)
        else:
            print('имеет 2 корня')
            x = (-b + math.sqrt(d)) / (2 * a)
            print(x)
            x = (-b - math.sqrt(d)) / (2 * a)
            print(x)


if __name__ == '__main__':
    a = float(input())
    b = float(input())
    c = float(input())
    tochki(a, b, c)