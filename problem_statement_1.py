even = False
array = []
while even is False:
    size = int(input('Total numbers of arrays you want to enter, it should be even: '))
    if size % 2 == 0:
        even = True
        for i in range(0, size):
            a = float(input(f'{i + 1}/{size} Enter first number '))
            b = float(input(f'{i + 1}/{size} Enter second number '))
            if 1.8 <= a / b <= 1.9:
                array.append(str([a, b]))
        print(f'Eureka {",".join(array)}')

    else:
        print('You entered even number, enter again')
