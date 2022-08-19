import random


def mix(array):
    for i in range(len(array)):
        random_index = random.randint(0,len(array)-1)
        temp = array[i]
        array[i] = array[random_index]
        array[random_index] = temp
    return array


if __name__ == "__main__":
    array = [random.randint(0, 1000) for i in range(10)]
    print(array)
    print(mix(array))