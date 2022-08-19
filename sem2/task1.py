# 1й способ
# def sum_figures(number):
#     while int(number) != number:
#         number = number * 10
#     sum = 0
#     for i in range(len(str(number))):
#         sum += number % 10
#         number = number // 10
#     return sum
# код закомментирован, потому что при умножении number на 10 мы получаем float с дополнительными числами на конце.
# Как этого избежать, я не додумался, поэтому решил решить задачу вторым способом. Хотел бы фидбэк получить, как это
# сделать, если вообще возможно :-)
def sum_figures(number):
    str_number = str(number)
    sum = 0
    for i in str_number:
        if i != ".":
            sum += int(i)
    return sum


if __name__ == "__main__":
    print(sum_figures(24.2345))
