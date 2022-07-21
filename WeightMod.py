import CircleTrainingData
from DatasetManager import m_data
from ColorPrint import fg

discriminator = 5 #Any shape after going through concatentateWeights that is lower than this number is classified as a circle, higher a square
learnRate = 0.6 #The value that is applied to the weights
datasetOriginal = []

weights = []

def applyWeights(dataset): #Multiplies all of the weights on their corrisponding values
    for x in range(len(dataset)):
        dataset[x] *= weights[x]

def concatenateWeights(dataset): #Adds all of the values together after being multiplied
    return sum(dataset)

def adjustWeights(rectangle, dataset): #Adjusts the weights based off of whether the AI was right or wrong, essentially is what 'trains' the AI
    global weights
    for x in range(len(weights)):
        if dataset[x] == 1:
            weights[x] += learnRate * (-1 if rectangle else 1)
    printWeights(weights)


def resetWeights(set): #Just sets all of the weights to their default values
    global weights
    for x in range(len(set)):
        print(len(set))
        weights.append(1)

def printWeights(weights):
    for i in range(12):
        print(weights[i*12:i*12+12])

def dispWeights(weights):
    line = ""
    for x in range(12):
        #TODO generalize this for datasets of different sizes
        line = ""
        for x in range(12):
            ""
dispWeights(weights)