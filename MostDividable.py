def ask_input():
    number_candidate = raw_input('Enter a maximum number: ')
    try:
        number_in = int(number_candidate)
        if number_in > 10000:
            print('This number is too big!\n')
            return ask_input()
        else:
            return number_in
    except ValueError:
        print('Invalid number!!\n')
        return ask_input()


num = ask_input()
totalDivs = 0
mostDivsNumber = 0
num_range = range(2, num + 1)
for number in num_range:
    numberOfDivs = 0
    for number2 in num_range:
        if number % number2 == 0:
            numberOfDivs += 1
    if numberOfDivs > totalDivs:
        totalDivs = numberOfDivs
        mostDivsNumber = number

print(
    '\nThe number {} has the most divisions between 0 and {}, with a total of {} divisions possible'.format(
        mostDivsNumber,
        num, totalDivs))
