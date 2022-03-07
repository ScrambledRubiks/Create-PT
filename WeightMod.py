import CircleTrainingData
from DatasetManager import data
discriminator = 5
learnRate = 0.6
datasetOriginal = []

weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
]

def applyWeights(dataset):
    for x in range(len(dataset)):
        if x < 144:
            dataset[x] = dataset[x] * weights[x]
    

def concatenateWeights(dataset):
    finalOutput = 0
    for x in range(len(dataset)):
        finalOutput = dataset[x] + finalOutput
    print(finalOutput)
    return finalOutput
    

def adjustWeights(rectangle, dataset):
    if rectangle == True:
        for x in range(len(weights)):
            x = int(x)
            if dataset[x] == 1:
                weights[x] = weights[x] - learnRate
            
    if rectangle == False:
        for x in range(len(weights)):
            if dataset[x] == 1:
                weights[x] = weights[x] + learnRate

def resetWeights():
    weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
]
