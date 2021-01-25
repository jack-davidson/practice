#!/usr/bin/env python3
import random

# Configuration:

# welcome the user and ask for their lottery number
welcome_message = "Welcome, please enter a lottery number"

# congratulate the user for winning the lotter
lottery_message_win = "Yay! You won the lottery"

# Make the user feel better if they do not win the lottery
lottery_message_loss = "Unfortunately, you did not win the lottery, good luck \
next time"

lottery_number_max = 999  # maximum lottery number
lottery_number_min = 0  # minimun lotter number


def main():
    print(welcome_message)  # Welcome the user and ask for their lottery number
    lottery_number_guess = input()  # Get the user's lottery number.

    # Random winning number defined in between a range of LOTTERY_NUMBER_MIN
    # and LOTTERY_NUMBER_MAX
    winning_number = random.randint(lottery_number_min, lottery_number_max)

    # compare the user's lottery number and the winning lottery number,
    # if it is the right number, print the LOTTERY_MESSAGE_WIN. Otherwise,
    # print the LOTTERY_MESSAGE_LOSS
    if winning_number == lottery_number_guess:
        print(lottery_message_win)
        return 0
    else:
        print(lottery_message_loss)
        return 0


if __name__ == "__main__":
    # consider future expansion of the program by returning shell exit codes
    # upon exit of main()
    exit(main())
