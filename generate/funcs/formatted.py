import math


def around_value(value):
    """
    Returns the floor of the input value
    
    :param value: The value to be rounded
    :return: The value of the input rounded to the nearest integer.
    """
    return math.floor(value + 0.5)


def clean_list(list_of_values):
    """
    This function takes a list of values and returns a list of values
    
    :param list_of_values: the list of values to be cleaned
    :return: A list of the first three values in the list_of_values parameter.
    """
    return [around_value(elem) for elem in list_of_values][0:3]


def reverse_percentage(percentage):
    """
    This functions get inverse of the input percentage

    :param percentage: The percentage of the data to use for training. The rest will be used for testing
    :return: The percentage of the total number of rows that are not null.
    """
    return 100-percentage


def get_percentage_between(value1, value2):
    """
    Returns the percentage between two values
    
    :param value1: The first value to compare
    :param value2: The value you want to compare to
    :return: The percentage change between the two values.
    """
    return ((value2 - value1) / value1 * 100)


def get_color_by_percentage(percentage):
    """
    Given a percentage, return a color
    
    :param percentage: The percentage of the query that was completed
    :return: a string.
    """
    if percentage >= 0 and percentage < 20:
        return "bE"
    elif percentage >= 20 and percentage < 40:
        return "bD"
    elif percentage >= 40 and percentage < 60:
        return "bC"
    elif percentage >= 60 and percentage < 80:
        return "bB"
    elif percentage >= 80:
        return "bA"
    else:
        return ""


def set_background_by_contast_color(color):
    """
    This function takes a color and returns a string based on the color's contrast
    
    :param color: The color to check
    :return: a string.
    """
    if color > (200, 200, 200):
        return "cnt"
    else:
        return ""
