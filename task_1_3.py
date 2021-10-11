for number in range(1, 101):
    if 4 < number <= 20:
        print(number, 'процентов')
    elif number % 10 == 1:
        print(number, 'процент')
    elif 1 < number % 10 < 5:
        print(number, 'процента')
    else:
        print(number, 'процентов')