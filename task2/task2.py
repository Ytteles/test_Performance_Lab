import math
import sys


def read_circle(circle_path_file: str) -> int:
    with open(circle_path_file, 'r') as file:
        center_circle_x, center_circle_y = map(int, file.readline().split())
        r = int(file.readline())
    return center_circle_x, center_circle_y, r


def read_dot(dot_path_file: str) -> list:
    dot_list = []
    with open(dot_path_file, 'r') as file:
        for line in file:
            dot_list.append(tuple(map(int, line.split())))
    return dot_list


def check_position(center_circle_x: int, center_circle_y: int, r: int, x: int, y: int) -> int:
    length = math.sqrt((x - center_circle_x) ** 2 + (y - center_circle_y) ** 2)
    if length == r:
        return 0
    elif length < r:
        return 1
    else:
        return 2


def classify_dot_circle():
    circle_path_file = sys.argv[1]
    dot_path_file = sys.argv[2]
    center_circle_x, center_circle_y, r = read_circle(circle_path_file)
    dots = read_dot(dot_path_file)
    for x, y in dots:
        print(check_position(center_circle_x, center_circle_y, r, x, y))


classify_dot_circle()
