while True:
    number = int(input('Введите день недели: '))
    if number == 6 or number == 7:
        print("да")
    elif number >= 1 and number <= 5:
        print("нет")
    else:
        print("Введен не день недели")