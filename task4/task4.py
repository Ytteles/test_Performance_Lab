import sys


def read_numbers(path_file: str) -> list[int]:
    with open(path_file, 'r') as file:
        return [int(i.strip()) for i in file]


def count_min_num_of_movies(numbers: list[int]) -> int:
    numbers.sort()
    median = numbers[len(numbers) // 2]
    return sum(map(lambda num: abs(num - median), numbers))


def res():
    path_file = sys.argv[1]
    nums = read_numbers(path_file)
    res = count_min_num_of_movies(nums)
    print(res)


res()
