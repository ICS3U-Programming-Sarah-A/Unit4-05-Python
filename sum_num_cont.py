#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr, 27, 2022
# This program asks the user to enter a number to determine how many numbers
# you want to add. After getting the number, it'll add those numbers until it
# reaches what user_num entered. Then it calculates all the numbers & displays
# the sum using loops & continue statements.

def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    while True:
        # get user input as string
        user_num_1_string = input("How many numbers would you like to add?: ")
        print("")

        try:
            # converts user input to integer
            user_num_1_int = int(user_num_1_string)

            if user_num_1_int >= 0:
                # calculate the sum of the entered numbers
                while (loop_counter < user_num_1_int):
                    # gets input from user
                    user_num_2_string = input("Enter a whole number: ")

                    try:
                        # converts entered number from string to integer
                        user_num_2_int = int(user_num_2_string)

                        # sets a range, as well as, adds the number entered.
                        if user_num_2_int >= 0:
                            print("{} has been added to the sum."
                                  .format(user_num_2_int))
                            print("")
                            sum = sum + user_num_2_int
                            loop_counter = loop_counter + 1
                        else:
                            print("{} is negative, so it cannot be added." .
                                  format(user_num_2_int))
                            print("")
                            continue
                    # handles the error case.
                    except Exception:
                        print("{} is not a number.". format(user_num_2_string))
                        print("")
                        continue
                # breaks out of the loop once counter & user reaches max
                if loop_counter == user_num_1_int:
                    print("The sum is = {}.".
                          format(sum))
                    break
            else:
                print("Please enter a whole number.")
                print("")
        # handles the error case.
        except Exception:
            print("{} is not a number.". format(user_num_1_string))
            print("")


if __name__ == "__main__":
    main()
