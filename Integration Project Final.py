"""John Holik: Macro Calculator and More!"""


# Used to store date into file so user can track progress
# Reformatting found on
# https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import date
import random

today = date.today()
today2 = today.strftime("%B %d, %Y")


def prompt_user():
    """This function prompts the user for an operator.The function checks to
    see if the user input is a valid operator. If the user input is not a valid
     operator, the function prints an error message and prompts the user again.
     The function returns the user input."""
    user_input = input("Enter an operator: ")
    if user_input in ['+', '-', '*', 'N', '/', '**', '%', '//', 'N']:
        return user_input
    else:
        print("Invalid operator")
        return prompt_user()


def show_calc_examples():
    """This function is used to show the user examples of the different
    functions that the calculator can do. It will continue to show examples
    until the user types 'N' to quit."""
    print("\n--------------------------------------------------------")
    print("The calculator can be used for many things.")
    print("To use it's basic functions please refer to the table "
          "below:")
    print("Use + and - (Add or Subtract) to add and subtract numbers.")
    print(
        "Use * or / (Multiply or Divide) to multiply and divide"
        "numbers.")
    print("Use ** (Exponent) to raise something to a power.")
    print("Use % (Modulus) to find the remainder.")
    print(
        "Use // (Floor Division) to divide and round to the nearest "
        "whole"
        " number.")
    calc_expression = prompt_user()
    calc_examples = True
    while calc_examples:
        if calc_expression == "+":
            print("You have chosen addition.")
            addition_value1 = int(input("Please input your first number: "))
            addition_value2 = int(input("Please input your second number: "))
            addition_output = addition_value1 + addition_value2
            print(addition_value1, '+', addition_value2, '=', addition_output,
                  sep="")
        elif calc_expression == "-":
            print("You have chosen subtraction.")
            subtraction_value1 = int(input("Please input your first number: "))
            subtraction_value2 = int(
                input("Please input your second number: "))
            subtraction_output = subtraction_value1 - subtraction_value2
            print(subtraction_value1, '-', subtraction_value2, '=',
                  subtraction_output, sep="")
        elif calc_expression == "*":
            print("You have chosen multiplication.")
            multi_value1 = int(input("Please input your first number: "))
            multi_value2 = int(input("Please input your second number: "))
            multi_output = multi_value1 * multi_value2
            print(multi_value1, '*', multi_value2, '=', multi_output, sep="")
        elif calc_expression == "/":
            print("You have chosen division.")
            divide_value1 = int(input("Please input your first number: "))
            divide_value2 = int(input("Please input your second number: "))
            divide_output = divide_value1 / divide_value2
            print(divide_value1, '/', divide_value2, '=',
                  format(divide_output, '.2f'), sep="")
        elif calc_expression == "**":
            print("You have chosen exponents.")
            expo_value1 = int(input("Please input your first number: "))
            expo_value2 = int(input("Please input your second number: "))
            expo_output = expo_value1 ** expo_value2
            print(expo_value1, '**', expo_value2, '=', expo_output, sep="")
        elif calc_expression == "%":
            print("You have chosen modulus.")
            mod_value1 = int(input("Please input your first number: "))
            mod_value2 = int(input("Please input your second number: "))
            mod_output = mod_value1 % mod_value2
            print(mod_value1, '%', mod_value2, '=', mod_output, sep="")
        elif calc_expression == "//":
            print("You have chosen floor division")
            floor_value1 = int(input("Please input your first number: "))
            floor_value2 = int(input("Please input your second number: "))
            floor_output = floor_value1 // floor_value2
            print(floor_value1, '//', floor_value2, '=', floor_output, sep="")
        print("If you would like to try another example type it's symbol. "
              "To quit type 'N'")
        calc_expression = prompt_user()
        if calc_expression == 'N':
            calc_examples = False
    print("Done!")


def get_input():
    """Asks the user for an input and then tests to make sure it is an int"""
    while True:
        try:
            user_input = int(input("Please enter a number: "))
            return user_input
        except ValueError:
            print("That is not a number. Please try again")


def macro_calc():
    """This function is used to calculate the macros of a meal.
It will ask the user to input the name of the meal, the amount of calories,
carbs, fat, sugar, and protein.
It will then write the data to a text file"""
    inFile = open("macroData.txt", 'a')
    inFile.write(today2)
    print("This is the macro calculator! Please type which meal you will"
          " be adding: ")
    meal_name = str(input())
    inFile.write("\nMeal:" + meal_name)
    print("You are now adding values for", meal_name)
    print("How many calories were in your meal: ")
    calories = str(get_input())
    inFile.write("\nCalories:" + calories)
    print("How many grams of carbs were in your meal: ")
    carbs = str(get_input())
    inFile.write("\nCarbs(g):" + carbs)
    print("How many grams of fat were in your meal: ")
    fat = str(get_input())
    inFile.write("\nFat(g):" + fat)
    print("How many grams of sugar were in your meal: ")
    sugar = str(get_input())
    inFile.write("\nSugar(g):" + sugar)
    print("How many grams of protein were in your meal: ")
    protein = str(get_input())
    inFile.write("\nProtein(g):" + protein)
    inFile.close()
    macro_data = open("macroData.txt")
    macro_data2 = macro_data.read()
    print("Added to list of meals: ")
    print(macro_data2)


def frog_attack():
    """This function is a simple program that prints out a frog for every
    number that the user inputs. The user must input a number between 1 and
    100."""
    x = 0
    user_input1 = None
    print("Are you ready to build your army of frogs?!!")
    input_control1 = True
    while input_control1:
        try:
            user_input1 = int(input("Please enter a number 1-100: "))
            if user_input1 > 100 or user_input1 < 1:
                print("Invalid input, please try again.")
                continue
            else:
                print("Get ready for a frog army!!!")
                input_control1 = False

        except ValueError:
            print("Invalid input, please try again.")
            continue
        input_control1 = False
    for i in range(0, user_input1):
        x += 1
        # Frog taken from POGIL 12
        print("  @."".@")
        print(" (----)")
        print("( >__< )")
        print("^^ ~~ ^^")
        print(x)
    print("THEY ARE EVERYWHERE!!!!!")


def gambling():
    """This function is a simple gambling game.The user is prompted to pick two
numbers between 1 and 50. The computer then picks two numbers between 1 and 50.
If one of the user's numbers matches one of the computer's numbers, the user
is congratulated for their luck. If the user's numbers do not match, the user
is told that they should not gamble."""
    user_input1 = None
    user_input2 = None
    print("So you think you're lucky?")
    print("Pick two numbers 1-50 and the computer will "
          "also pick two numbers 1-50.")
    print("If you really are lucky one of your numbers will be the same!")
    input_control1 = True
    while input_control1:
        try:
            user_input1 = int(input("Please enter a number 1-50: "))
            if user_input1 > 50 or user_input1 < 1:
                print("Invalid input, please try again.")
                continue
            else:
                input_control1 = False
                print("Your first number is", user_input1)
        except ValueError:
            print("Invalid input, please try again.")
            continue
    input_control2 = True
    while input_control2:
        try:
            user_input2 = int(input("Please enter a number 1-50: "))
            if user_input2 > 50 or user_input2 < 1:
                print("Invalid input, please try again.")
                continue
            else:
                input_control2 = False
                print("Your second number is", user_input2)
        except ValueError:
            print("Invalid input, please try again.")
            continue
    comp_num = random.randint(1, 50)
    comp_num2 = random.randint(1, 50)
    print("The computer picked", comp_num, "and", comp_num2)
    if user_input1 == comp_num and user_input2 == comp_num2:
        print("Wow you're incredibly lucky. "
              "You should go buy a lottery ticket!")
    else:
        print("Your numbers did not match. This is why you shouldn't gamble.")


def main():
    """This is the main function for the program. All other functions can be
    accessed through this by using a menu system and inputting a number 1-5."""
    user_input = None
    print("Welcome to John's Macro Calculator!")
    print(
        "To see examples of the possible functions the calculator can perform"
        " type '1', to use the macro calculator type '2', to try out some "
        "to be a victim of a frog attack type '3', to gamble type '4', "
        "to quit type '5'.")
    functions = False
    inputControl = True
    while inputControl:
        try:
            user_input = int(input("Please enter a number 1-5: "))
            if user_input > 5 or user_input < 1:
                print("Invalid input, please try again.")
                continue
            else:
                inputControl = False
                functions = True
        except ValueError:
            print("Invalid input, please try again.")
            continue

    while functions:
        if user_input == 1:
            functions = False
            show_calc_examples()
        elif user_input == 2:
            functions = False
            macro_calc()
        elif user_input == 3:
            functions = False
            frog_attack()
        elif user_input == 4:
            functions = False
            gambling()
        elif user_input == 5:
            print("Done!")
            break


main()
