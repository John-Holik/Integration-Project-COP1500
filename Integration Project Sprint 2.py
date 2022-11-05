# Integration Project Sprint #2 John Holik
# Macro Calculator

# Used to store date into file so user can track progress
# Reformatting found on
# https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import date

today = date.today()
today2 = today.strftime("%B %d, %Y")


# Calculator Examples

def show_calc_examples(calc_expression):
    # Below is a list that is used to make sure the users inputs a proper
    # function and will continue to prompt an input until they put in an
    # accepted value
    functions = ['+', '-', '*', 'N', '/', '**', '%', '//', 'N']
    calc_examples = True
    while calc_examples:
        if calc_expression == "+":
            print("You have chosen addition.")
            addition_value1 = int(input("Please input your first number: "))
            addition_value2 = int(input("Please input your second number: "))
            addition_output = addition_value1 + addition_value2
            print(addition_value1, '+', addition_value2, '=', addition_output,
                  sep="")
        if calc_expression == "-":
            print("You have chosen subtraction.")
            subtraction_value1 = int(input("Please input your first number: "))
            subtraction_value2 = int(
                input("Please input your second number: "))
            subtraction_output = subtraction_value1 - subtraction_value2
            print(subtraction_value1, '-', subtraction_value2, '=',
                  subtraction_output, sep="")
        if calc_expression == "*":
            print("You have chosen multiplication.")
            multi_value1 = int(input("Please input your first number: "))
            multi_value2 = int(input("Please input your second number: "))
            multi_output = multi_value1 * multi_value2
            print(multi_value1, '*', multi_value2, '=', multi_output, sep="")
        if calc_expression == "/":
            print("You have chosen division.")
            divide_value1 = int(input("Please input your first number: "))
            divide_value2 = int(input("Please input your second number: "))
            divide_output = divide_value1 / divide_value2
            print(divide_value1, '/', divide_value2, '=',
                  format(divide_output, '.2f'), sep="")
        if calc_expression == "**":
            print("You have chosen exponents.")
            expo_value1 = int(input("Please input your first number: "))
            expo_value2 = int(input("Please input your second number: "))
            expo_output = expo_value1 ** expo_value2
            print(expo_value1, '**', expo_value2, '=', expo_output, sep="")
        if calc_expression == "%":
            print("You have chosen modulus.")
            mod_value1 = int(input("Please input your first number: "))
            mod_value2 = int(input("Please input your second number: "))
            mod_output = mod_value1 % mod_value2
            print(mod_value1, '%', mod_value2, '=', mod_output, sep="")
        if calc_expression == "//":
            print("You have chosen floor division")
            floor_value1 = int(input("Please input your first number: "))
            floor_value2 = int(input("Please input your second number: "))
            floor_output = floor_value1 // floor_value2
            print(floor_value1, '//', floor_value2, '=', floor_output, sep="")
        print("If you would like to try another example type it's symbol. "
              "To quit type 'N'")
        # Checks to make sure the user inputs a proper value
        calc_expression = ' '
        while calc_expression not in functions:
            calc_expression = input("Enter a function symbol or 'N': ")
        if calc_expression == 'N':
            calc_examples = False
    print("Done!")


def main_calc():
    # Opens the file macrodata.txt to start writing to it so the user can
    # keep track of their data
    inFile = open("macroData.txt", 'a')
    inFile.write(today2)
    print("This is the macro calculator! Please type which meal you will"
          " be adding: ")
    meal_name = str(input())
    inFile.write("\nMeal:" + meal_name)
    print("You are now adding values for", meal_name)
    print("How many calories were in your meal: ")
    calories = str(input())
    inFile.write("\nCalories:" + calories)
    print("How many grams of carbs were in your meal: ")
    carbs = str(input())
    inFile.write("\nCarbs(g):" + carbs)
    print("How many grams of fat were in your meal: ")
    fat = str(input())
    inFile.write("\nFat(g):" + fat)
    print("How many grams of sugar were in your meal: ")
    sugar = str(input())
    inFile.write("\nSugar(g):" + sugar)
    print("How many grams of protein were in your meal: ")
    protein = str(input())
    inFile.write("\nProtein(g):" + protein)
    inFile.close()
    macro_data = open("macroData.txt")
    macro_data2 = macro_data.read()
    print("Added to list of meals: ")
    print(macro_data2)


def frog_attack():
    x = 0
    print("These are some extra functions that I need to use for my "
          "integration project. Sit back and enjoy the ride!")
    input_control = True
    while input_control:
        try:
            user_input = int(input("Chose a number 1 - 100: "))
        except:
            print("Invalid selection. Try again.")
        else:
            int_control = True
            input_control = False
    while int_control:
        if user_input < 1 or user_input > 100:
            print("Invalid selection. Try again.")
            int_control = False
        else:
            print("Get ready for a frog army!!!")
            int_control = False
    for i in range(0, user_input):
        x += 1
        # Frog taken from POGIL 12
        print("  @."".@")
        print(" (----)")
        print("( >__< )")
        print("^^ ~~ ^^")
        print(x)
    print("THEY ARE EVERYWHERE!!!!!")


import random


def gambling():
    print("So you think you're lucky?")
    print("Pick two numbers 1-50 and the computer will "
          "also pick two numbers 1-50.")
    print("If you really are lucky one of your numbers will be the same!")
    input_control = True
    while input_control:
        try:
            user_input1 = int(input("Chose a number 1 - 50: "))
        except:
            print("Invalid selection. Try again.")
        else:
            int_control = True
            input_control = False
    while int_control:

        if user_input1 < 1 or user_input1 > 50:
            print("Invalid selection. Try again.")
            int_control = False
        else:
            print("Your first number is", user_input1)
            int_control = False
    input_control = True
    while input_control:
        try:
            user_input2 = int(input("Chose another number 1 - 50: "))
        except:
            print("Invalid selection. Try again.")
        else:
            int_control = True
            input_control = False
    while int_control:
        if user_input2 < 1 or user_input2 > 50:
            print("Invalid selection. Try again.")
            int_control = False
        else:
            print("Your second number is", user_input2)
            int_control = False
    comp_num = random.randint(1, 50)
    comp_num2 = random.randint(1, 50)
    print("The computer picked", comp_num, "and", comp_num2)
    if user_input1 == comp_num and user_input2 == comp_num2:
        print("Wow you're incredibly lucky. "
              "You should go buy a lottery ticket!")
    else:
        print("Your numbers did not match. This is why you shouldn't gamble.")


# Main Function that makes calls to all other functions in the program

def main():
    print("Welcome to John's Macro Calculator!")
    print(
        "To see examples of the possible functions the calculator can perform"
        " type '1', to use the macro calculator type '2', to try out some "
        "to be a victim of a frog attack type '3', to gamble type '4', "
        "to quit type '5'.")
    inputControl = True
    while inputControl:
        try:
            calc_or_examples = int(input())
        except:
            print("Invalid selection. Try again.")
        else:
            intControl = True
            inputControl = False
    while intControl:
        if calc_or_examples < 1 or calc_or_examples > 4:
            print("Invalid selection. Try again.")
            intControl = False

        elif calc_or_examples == 5:
            intControl = False
            print("Done!")
        else:
            functions = True
            intControl = False
    while functions:
        if calc_or_examples == 1:
            functions = False
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
            calc_example = input("To use a function please input it's symbol:"
                                 " ")
            show_calc_examples(calc_example)
        elif calc_or_examples == 2:
            functions = False
            main_calc()
        elif calc_or_examples == 3:
            functions = False
            frog_attack()
        elif calc_or_examples == 4:
            functions = False
            gambling()


main()
