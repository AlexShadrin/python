# A
price = [57.8, 46.51, 97, 11, 27.43, 31.32, 49.02, 54.94, 9.01, 101, 5, 66.27]
for position in price:
    r = int(position)
    kk = (position - int(position)) * 100
    print(f'{r} руб {kk:02.0f} коп', end=', ')

# B
price = [57.8, 46.51, 97, 11, 27.43, 31.32, 49.02, 54.94, 9.01, 101, 5, 66.27]
print(id(price))
price.sort()
print(id(price))
for position in price:
    r = int(position)
    kk = (position - int(position)) * 100
    print(f'{r} руб {kk:02.0f} коп')

# C
price = [57.8, 46.51, 97, 11, 27.43, 31.32, 49.02, 54.94, 9.01, 101, 5, 66.27]
for position in sorted(price)[::-1]:
    r = int(position)
    kk = (position - int(position)) * 100
    print(f'{r} руб {kk:02.0f} коп')

# D
price = [57.8, 46.51, 97, 11, 27.43, 31.32, 49.02, 54.94, 9.01, 101, 5, 66.27]
for position in sorted(price)[::][7:]:
    r = int(position)
    kk = (position - int(position)) * 100
    print(f'{r} руб {kk:02.0f} коп')