my_list = []
for number in range(1, 1001, 2):
    my_list.append(number ** 3)
required_amount = 0  # Решение для задачи a.
for number in my_list:
    preliminary_amount = 0
    for provisional_number in str(number):
        preliminary_amount += int(provisional_number)
    if preliminary_amount % 7 == 0:
        required_amount += number
print(required_amount)
required_amount = 0     # Решение для задач b и c.
for number in my_list:
    number += 17
    preliminary_amount = 0
    for provisional_number in str(number):
        preliminary_amount += int(provisional_number)
    if preliminary_amount % 7 == 0:
        required_amount += number
print(required_amount)