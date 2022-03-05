discriminator = 1
learnRate = 0.6

weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, #each weight can be a value between -2 and 3
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
    for x in dataset:
        dataset[x] = dataset[x] * weights[x]

def concatenateWeights(dataset):
    finalOutput = discriminator
    for x in dataset:
        finalOutput = dataset[x] + finalOutput
    return finalOutput

def adjustWeights(rectangle, dataset):
    if rectangle == True:
        for x in weights:
            x = int(x)
            if dataset[x] == 1:
                weights[x] = weights[x] - learnRate
            
    if rectangle == False:
        for x in weights:
            if dataset[x] == 0:
                weights[x] = weights[x] + learnRate