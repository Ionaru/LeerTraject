def ask_input():
    number_candidate = raw_input('Enter a maximum number: ')
    maximum_num = 1000000
    try:
        number = int(number_candidate)
        if number > maximum_num:
            print('This number is too big!\n')
            return ask_input()
        else:
            return number
    except ValueError:
        print('Invalid number!!\n')
        return ask_input()


num = int(ask_input())
num_range = range(2, num)
for number1 in num_range:
    numberOfDivs = 0
    for number2 in num_range:
        if number1 % number2 == 0:
            numberOfDivs += 1
    if numberOfDivs == 1:
        # print '\n%s is a prime number!' % (num,)

        numberL = list(str(number1))
        total = 0
        for numberI in numberL:
            total += (int(numberI) * int(numberI))
        tries = 0
        while total != 1 and tries != 5:
            tries += 1
            numberL = list(str(total))
            total = 0
            for numberI in numberL:
                total += (int(numberI) * int(numberI))
        if total == 1:
            print('{} is a happy prime! :D'.format(number1))
