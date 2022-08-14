while True:
    x = int(input("Введите X: "))
    if x == 0:
        print("X не может быть равно 0")
        continue
    else:
        break
while True:
    y = int(input("Введите Y: "))
    if y == 0:
        print("Y не может быть равно 0")
        continue
    else:
        break
if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")