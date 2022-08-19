import random


def multiply(n):
    array = [random.randint(-n, n) for i in range(n)]
    print(array)
    result = 1
    with open("file.txt") as file:
        str1 = file.readline()
        while str1 != "":
            result = result * array[int(str1)]
            str1 = file.readline()
    return result


if __name__ == "__main__":
    print(multiply(5))
