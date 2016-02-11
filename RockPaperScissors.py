def ask_input():
    choice = raw_input()
    try:
        choice_str = str(choice.lower().title())
        if choice_str == "Rock" or choice_str == "Paper" or choice_str == "Scissors":
            return choice_str
        else:
            print "Invalid input, please choose between Rock, Paper and Scissors:"
            return ask_input()
    except ValueError:
        print "Invalid input, please try again:"
        return ask_input()

print "---< Welcome to Rock Paper Scissors, enjoy the game! >---"
while True:
    print "\n\nPlayer 1: Rock, Paper or Scissors? "
    p1 = ask_input()
    print "Player 1 chose %s\n" % (p1, )
    print "\nPlayer 2: Rock, Paper or Scissors? "
    p2 = ask_input()
    print "Player 2 chose %s\n\n" % (p2, )
    if p1 == p2:
        print "It's a draw!"
    elif p1 == "Paper" and p2 == "Rock":
        print "Paper beats Rock, player 1 wins!"
    elif p1 == "Scissors" and p2 == "Rock":
        print "Rock beats Scissors, player 2 wins!"
    elif p1 == "Rock" and p2 == "Paper":
        print "Paper beats Rock, player 2 wins!"
    elif p1 == "Scissors" and p2 == "Paper":
        print "Scissors beats Paper, player 1 wins!"
    elif p1 == "Rock" and p2 == "Scissors":
        print "Rock beats Scissors, player 1 wins!"
    elif p1 == "Paper" and p2 == "Scissors":
        print "Scissors beats Paper, player 2 wins!"
