import sys


def read_numbers(path_file: str) -> list[int]:
    with open(path_file, 'r') as file:
        return [int(i.strip()) for i in file]


def min_num_for_movies(numbers: list[int]) -> int:
    numbers.sort()
    median = numbers[len(numbers) // 2]
    return sum(map(lambda num: abs(num - median), numbers))


def main():
    if len(sys.argv) != 2:
        print('Используйте такое написание: python3 task4.py numbers.txt')
        return

    path_file = sys.argv[1]
    nums = read_numbers(path_file)

    res = min_num_for_movies(nums)
    print(res)


main()
