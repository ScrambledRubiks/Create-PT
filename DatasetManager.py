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
        return getattr(RectangleTrainingData,  str("rectangleSet" + str(random.randint(0,9))))

    def YNtoTF(var):
        if var == "y":
            return True
        elif var == "n":
            return False
        else:
            print("Invalid response.")