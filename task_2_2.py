my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
desired_list = []
for position in my_list:
    if position.isdigit():
        desired_list.extend(['"', f'{int(position):02}', '"'])
    elif position.startswith('+') and position[1:].isdigit():
        desired_list.extend(['"', f'{position[0]}{int(position[1:]):02}', '"'])
    else:
        desired_list.append(position)
ready_list = ' '.join(desired_list)
print(ready_list)