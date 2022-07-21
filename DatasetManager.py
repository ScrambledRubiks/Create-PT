import random
import CircleTrainingData
import RectangleTrainingData
from DatasetImport import m_import
from Setup import s

class m_data(): #This class as well as the weird way I am importing functions from this file into UserProtocol.py is necessary for some reason
    def RandDataset(): #Just grabs a random dataset
        return random.choice([
            m_data.randCircle,
            m_data.randRectangle,
        ])()

    def randCircle():
        return [x for x in getattr(CircleTrainingData,  str("circleSet" + str(random.randint(0,9))))]

    def randRectangle():
        return [x for x in getattr(RectangleTrainingData,  str("RectangleSet" + str(random.randint(0,9))))]

    def YNtoTF(var):
        if var == "y":
            return True
        elif var == "n":
            return False
        else:
            print("Invalid response.")
            return True

    def DisplayDataset(dataset):
        displayLine = ""
        index = -1
        for x in range(m_import.initData(s.activeSets[0])[0]):
            for y in range(m_import.initData(s.activeSets[0])[1]): #This nested for loop makes sure it prints out 12 'pixels' per line, 12 times due to the datasets being 12x12
                index = index + 1
                if dataset[index] == 0:
                    displayLine += "░░░"
                elif dataset[index] == 1:
                    displayLine += "███"
                else:
                    print("Corrupt dataset")
                    return 
            print(displayLine)
            displayLine = ""
    
    m_import.initData("rectangle")
    print(m_import.getData("rectangle", 0))
    DisplayDataset(m_import.getData("rectangle", 0))



