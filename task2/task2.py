import math
import sys


def read_circle(path_circle: str) -> int:
    with open(path_circle, 'r') as file:
        center_circle_x, center_circle_y = map(int, file.readline().split())
        r = int(file.readline().strip())
    return center_circle_x, center_circle_y, r


def read_dot(path_dot: str) -> list:
    dot = []
    with open(path_dot, 'r') as file:
        for line in file:
            dot.append(tuple(map(int, line.split())))
    return dot


def check_position(center_circle_x: int, center_circle_y: int, r: int, x: int, y: int) -> int:
    distance = math.sqrt((x - center_circle_x) ** 2 + (y - center_circle_y) ** 2)
    if math.isclose(distance, r):
        return 0  # точка на окружности
    elif distance < r:
        return 1  # точка внутри окружности
    else:
        return 2  # точка снаружи окружности


def classify_dot_circle():
    if len(sys.argv) != 3:
        print('Используйте такое написание: python3 task2.py circle.txt dot.txt')
        return

    circle_file = sys.argv[1]
    dot_file = sys.argv[2]

    xc, yc, r = read_circle(circle_file)
    dots = read_dot(dot_file)

    for x, y in dots:
        print(check_position(xc, yc, r, x, y))


classify_dot_circle()
