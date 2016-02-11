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
x = range(2, num)
numberOfDivs = 0
for elem in x:
    if num % elem == 0:
        numberOfDivs += 1
        print elem
if numberOfDivs == 0:
    print('\n{} is a prime number!'.format(num))
else:
    print('\nThis number can be divided by {} other numbers.'.format(numberOfDivs))
