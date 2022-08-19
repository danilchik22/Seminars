def sum(n):
    array = [1 + 1 / i for i in range(1, n + 1)]
    sum = 0
    for i in array:
        sum += i
    print(array) # вывел список, чтобы легче было ориентироваться
    return sum


if __name__ == "__main__":
    print(sum(5))
