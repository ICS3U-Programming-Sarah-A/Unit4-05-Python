#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr, 27, 2022
# This program asks the user to enter a number to determine how many numbers
# you want to add. After getting the number, it'll add those numbers until it
# reaches what user_num entered. Then it calculates all the numbers & displays
# the sum.


def main():
    # initialize the loop counter and sum
    sum = 0
    counter = 0

    while True:
        # get the user number as a string
        user_number_string_1 = input("How many numbers \
            would you like to add? ")
        print("")

        try:
            # converts user input to integer
            user_num_int_1 = int(user_number_string_1)

            if user_num_int_1 >= 0:
                while (counter < user_num_int_1):
                    # get user input 2
                    user_num_string_2 = input("Enter a whole number: ")
                    try:
                        # converts user input to an integer
                        user_num_int_2 = int(user_num_string_2)
                        # sets a range
                        if user_num_int_2 >= 0:
                            print("{} has been added to the sum.".
                                  format(user_num_int_2))
                            print("")
                            sum = sum + user_num_int_2
                            counter = counter + 1
                            continue
                        else:
                            print("{} is a negative number, so\
                                it was not added".format(user_num_int_2))
                            continue
                    # handles error case
                    except Exception:
                        print("{} is not a valid number".
                              format(user_num_string_2))
                        continue
                    # breaks out of the loop once counter & user reaches max
                    if counter == user_num_int_1:
                        print("The sum is = {}.".
                              format(sum))
                        break
            else:
                print("Please enter a whole number.")
        # handles error case
        except Exception:
            print("{} is not a valid number.". format(user_number_string_1))


if __name__ == "__main__":
    main()
