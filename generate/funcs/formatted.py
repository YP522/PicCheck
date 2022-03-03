import math


def aroundValue(value):
    return math.floor(value + 0.5)


def cleanList(listOfValues):
    return [aroundValue(elem) for elem in listOfValues][0:3]


def reversePercentage(percentage):
    return 100-percentage


def getPercentageBetween(value1, value2):
    return ((value2 - value1) / value1 * 100)


def getColorByPercentage(percentage):
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


def setBackgroundByContastColor(color):
    if color > (200, 200, 200):
        return "cnt"
    else:
        return ""
