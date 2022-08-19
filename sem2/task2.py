import math


# 1-й способ
def multiply(number):
    array = [math.factorial(i) for i in range(1, number + 1)]
    return array


# 2-й способ
def multiply_2(number):
    array = [1]
    for i in range(1, number + 1):
        array.append(array[i - 1] * i)
    return array[1:]


if __name__ == "__main__":
    print(multiply(10))
    print(multiply_2(10))
