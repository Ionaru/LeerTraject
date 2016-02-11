def check_number(number):
    if int(number) % 2 == 0:
        return True
    return False


def ask_input():
    number_candidate = raw_input("Enter a number to check: ")
    try:
        return int(number_candidate)
    except ValueError:
        print "Invalid number!!\n"
        return ask_input()


if check_number(ask_input()):
    print "Number is even!"
else:
    print "Number is uneven!"
