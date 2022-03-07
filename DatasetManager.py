import random
import CircleTrainingData
import RectangleTrainingData

class data():
    def RandDataset():
        if random.randint(0,1) == 0:
            return getattr(CircleTrainingData,  str("circleSet" + str(random.randint(0,9))))
        else:
            return getattr(RectangleTrainingData,  str("RectangleSet" + str(random.randint(0,9))))

    def randCircle():
        return getattr(CircleTrainingData,  str("circleSet" + str(random.randint(0,9))))

    def randRectangle():
        return getattr(RectangleTrainingData,  str("RectangleSet" + str(random.randint(0,9))))

    def YNtoTF(var):
        if var == "y":
            return True
        elif var == "n":
            return False
        else:
            print("Invalid response.")

    def DisplayDataset(dataset):
        displayLine = ""
        index = -1
        for x in range(12):
            for y in range(12):
                index = index + 1
                if dataset[index] == 0:
                    displayLine = displayLine + "░░░"
                elif dataset[index] == 1:
                    displayLine = displayLine + "███"
                else:
                    displayLine = displayLine + "███"
            print(displayLine)
            displayLine = ""
            
