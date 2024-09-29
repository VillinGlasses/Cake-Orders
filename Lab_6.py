"""
***************************************************************************
Filename:      lab_6.py

Author:        Ankit Bombwal

Date:          2020.07.18

Modifications: Ankit Bombwal – 2020.07.24

Description:   This module demonstrates the use of functions to:
               1) Open a file to read in orders from a text file.
               2) Output the ingredient lists to another file.
               3) Loop until the orders file is empty.

***************************************************************************
"""


def chocolate_cake(cake_weight):
    """
    *********************************************************************************
    Function: chocolate_cake(cake_weight)
    Parameters: cake_weight - the weight of the cake in ounces.
    Outputs: Prints the weight of each ingredient in ounces.
    Returns: None
    Author: Ankit Bombwal
    Date: 2020.07.18
    Modifications: 2020.07.24
    Description: This function calculates the weight of each ingredient
    for a large or regular sized chocolate cake and outputs them to a separate file.
    *********************************************************************************
    """
    # Calculating the weight of each ingredient, rounding to the tenths place.
    flour = round(cake_weight * 0.158, 1)
    sugar = round(cake_weight * 0.245, 1)
    cocoa_powder = round(cake_weight * 0.056, 1)
    baking_powder = round(cake_weight * 0.004, 1)
    baking_soda = round(cake_weight * 0.006, 1)
    salt = round(cake_weight * 0.004, 1)
    egg = round(cake_weight * 0.09, 1)
    buttermilk = round(cake_weight * 0.180, 1)
    canola_oil = round(cake_weight * 0.081, 1)
    vanilla_extract = round(cake_weight * 0.006, 1)
    boiling_water = round(cake_weight * 0.170, 1)

    # opening relevant file information
    cake_file = open("cake_ingredients_list.txt", "a")

    # Outputs ingredient list to the screen.
    if cake_weight == 64:
        cake_file.write("Ingredients for a regular chocolate cake: \n")
    elif cake_weight == 112:
        cake_file.write("Ingredients for a large chocolate cake: \n")
    cake_file.write("Flour: " + str(flour) + " Oz \n")
    cake_file.write("Sugar: " + str(sugar) + " Oz \n")
    cake_file.write("Unsweetened Cocoa Powder: " + str(cocoa_powder) + " Oz \n")
    cake_file.write("Baking Powder: " + str(baking_powder) + " Oz \n")
    cake_file.write("Baking Soda: " + str(baking_soda) + " Oz \n")
    cake_file.write("Salt: " + str(salt) + " Oz \n")
    cake_file.write("Egg: " + str(egg) + " Oz \n")
    cake_file.write("Buttermilk: " + str(buttermilk) + " Oz \n")
    cake_file.write("Canola Oil: " + str(canola_oil) + " Oz \n")
    cake_file.write("Vanilla Extract: " + str(vanilla_extract) + " Oz \n")
    cake_file.write("Boiling Water: " + str(boiling_water) + " Oz \n")
    cake_file.write("\n")
    cake_file.close()


def red_velvet(cake_weight):
    """
    **********************************************************************************
    Function: red_velvet(cake_weight)
    Parameters: cake_weight - the weight of the cake in ounces.
    Outputs: Prints the weight of each ingredient in ounces.
    Returns: None
    Author: Ankit Bombwal
    Date: 2020.07.18
    Modifications: 2020.07.24
    Description: This function calculates the weight of each ingredient
    for a large or regular sized red velvet cake and outputs them to a separate file.
    **********************************************************************************
    """
    # Calculating the weight of each ingredient, rounding to the tenths place.
    flour = round(cake_weight * 0.224, 1)
    sugar = round(cake_weight * 0.224, 1)
    baking_soda = round(cake_weight * 0.007, 1)
    salt = round(cake_weight * 0.004, 1)
    cocoa_powder = round(cake_weight * 0.004, 1)
    canola_oil = round(cake_weight * 0.240, 1)
    buttermilk = round(cake_weight * 0.179, 1)
    egg = round(cake_weight * 0.090, 1)
    red_coloring = round(cake_weight * 0.021, 1)
    vanilla_extract = round(cake_weight * 0.003, 1)
    vinegar = round(cake_weight * 0.004, 1)

    # opening relevant file information
    cake_file = open("cake_ingredients_list.txt", "a")

    # Outputs ingredient list to the screen.
    if cake_weight == 64:
        cake_file.write("Ingredients for a regular red velvet cake: \n")
    elif cake_weight == 112:
        cake_file.write("Ingredients for a large red velvet cake: \n")
    cake_file.write("Flour: " + str(flour) + " Oz \n")
    cake_file.write("Sugar: " + str(sugar) + " Oz \n")
    cake_file.write("Baking Soda: " + str(baking_soda) + " Oz \n")
    cake_file.write("Salt: " + str(salt) + " Oz \n")
    cake_file.write("Unsweetened Cocoa Powder: " + str(cocoa_powder) + " Oz \n")
    cake_file.write("Canola Oil: " + str(canola_oil) + " Oz \n")
    cake_file.write("Buttermilk: " + str(buttermilk) + " Oz \n")
    cake_file.write("Egg: " + str(egg) + " Oz \n")
    cake_file.write("Red Food Coloring: " + str(red_coloring) + " Oz \n")
    cake_file.write("Vanilla Extract: " + str(vanilla_extract) + " Oz \n")
    cake_file.write("Distilled Vinegar: " + str(vinegar) + " Oz \n")
    cake_file.write("\n")
    cake_file.close()


def lemon_cake(cake_weight):
    """
    *****************************************************************************
    Function: lemon_cake(cake_weight)
    Parameters: cake_weight - the weight of the cake in ounces.
    Outputs: Prints the weight of each ingredient in ounces.
    Returns: None
    Author: Ankit Bombwal
    Date: 2020.07.18
    Modifications: 2020.07.24
    Description: This function calculates the weight of each ingredient
    for a large or regular sized lemon cake and outputs them to a separate file.
    *****************************************************************************
    """
    # Calculating the weight of each ingredient, rounding to the tenths place.
    butter = round(cake_weight * 0.085, 1)
    sugar = round(cake_weight * 0.150, 1)
    egg = round(cake_weight * 0.090, 1)
    self_rising_flour = round(cake_weight * 0.156, 1)
    buttermilk = round(cake_weight * 0.090, 1)
    vanilla_extract = round(cake_weight * 0.002, 1)
    filling_egg_yolk = round(cake_weight * 0.179, 1)
    filling_sugar = round(cake_weight * 0.113, 1)
    filling_butter = round(cake_weight * 0.021, 1)
    filling_lemon_juice_and_zest = round(cake_weight * 0.114, 1)

    # opening relevant file information
    cake_file = open("cake_ingredients_list.txt", "a")

    # Outputs ingredient list to the screen.
    if cake_weight == 64:
        cake_file.write("Ingredients for a regular lemon cake: \n")
    elif cake_weight == 112:
        cake_file.write("Ingredients for a large lemon cake: \n")
    cake_file.write("Butter: " + str(butter) + " Oz \n")
    cake_file.write("Sugar: " + str(sugar) + " Oz \n")
    cake_file.write("Egg: " + str(egg) + " Oz \n")
    cake_file.write("Self-Rising Flour: " + str(self_rising_flour) + " Oz \n")
    cake_file.write("Buttermilk: " + str(buttermilk) + " Oz \n")
    cake_file.write("Vanilla Extract: " + str(vanilla_extract) + " Oz \n")
    cake_file.write("Filling - Egg Yolk: " + str(filling_egg_yolk) + " Oz \n")
    cake_file.write("Filling - Sugar: " + str(filling_sugar) + " Oz \n")
    cake_file.write("Filling - Butter: " + str(filling_butter) + " Oz \n")
    cake_file.write("Filling - Lemon Juice and Zest: " + str(filling_lemon_juice_and_zest) + " Oz \n")
    cake_file.write("\n")
    cake_file.close()


def cake_info_gather():
    """
    *************************************************************************
    Function: cake_info_gather()
    Parameters: None
    Outputs: Prints a string to confirm choice
             or invalid inputs.
    Returns: None
    Author: Ankit Bombwal
    Date: 2020.07.18
    Modifications: 2020.07.24
    Description: This function reads in data from a separate file and calls
                 The necessary function based on built-in logic.
    *************************************************************************
    """
    # Cake sizes in ounces.
    REGULAR_CAKE = 64
    LARGE_CAKE = 112
    # Gathering user input
    # Place Loop Starting Here
    handle_name = open("cake_orders.txt")
    while True:
        cake_type = eval(handle_name.read(1))
        spaces = handle_name.read(3)
        cake_size = handle_name.read(1)
        loop_query = handle_name.read(1)

        # Cake Decision if/else
        if cake_type == 1:
            if cake_size == 'R':
                chocolate_cake(REGULAR_CAKE)
            elif cake_size == 'L':
                chocolate_cake(LARGE_CAKE)
            else:
                print("Error, invalid input!")
        elif cake_type == 2:
            if cake_size == 'R':
                red_velvet(REGULAR_CAKE)
            elif cake_size == 'L':
                red_velvet(LARGE_CAKE)
            else:
                print("Error, invalid input!")
        elif cake_type == 3:
            if cake_size == 'R':
                lemon_cake(REGULAR_CAKE)
            elif cake_size == 'L':
                lemon_cake(LARGE_CAKE)
            else:
                print("Error, invalid input!")
        else:
            print("Error, invalid input!")
        if loop_query == '':
            break
    handle_name.close()


cake_info_gather()
