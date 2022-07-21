from re import M
from Setup import s
import WeightMod
from DatasetManager import m_data
from DatasetImport import m_import
import random

command = ""
currentSet = []
answer = ""
WeightMod.resetWeights(m_data.RandDataset())
m_import.initData(s.activeSets[0]) #TODO generalize for 3 or more active sets
m_import.initData(s.activeSets[1])

def getAnswer():
    #TODO generalize for 3 or more active sets
    if random.randint(0,1) == 1:
        currentSet =  m_import.getData(s.activeSets[1])
    else:
        currentSet = m_import.getData(s.activeSets[0])
    
    m_data.DisplayDataset(currentSet) #Prints this dataset to the screen
    WeightMod.datasetOriginal = [x for x in currentSet] #datasetOriginal is kind of redundant but it can fix some issues sometimes
    WeightMod.applyWeights(currentSet) #Multiplies the weight values with the current dataset
    return getAnswer(currentSet)
    if WeightMod.concatenateWeights(currentSet) > WeightMod.discriminator:
        return True
    else:
        return False
def trainAI(UserInput): #This is the primary function that pulls all of the different aspects of the AI into one user interface.
    global currentSet
    global answer

    if UserInput: #UserInput is a boolean reperesenting whether the user decides to give they AI a circle/rectangle or decide to have it be chosen randomly
        print("Should the AI be shown a circle or a rectangle?")  
        command4 = input("c/r: ")
        if command4 == "c":
            currentSet = m_data.randCircle()
            answer =  getAnswer(currentSet)
            print(answer)
            if answer >= WeightMod.discriminator:
                print("The AI incorrectly guessed that this was a rectangle.")
                WeightMod.adjustWeights(True,  WeightMod.datasetOriginal) #Gives the AI feedback by subtracting each falsely positive weight value by the learning rate
            else:
                print("The AI correctly guessed that this is a circle.")
            trainAI(True)
        elif command4 == "r":
            currentSet = m_data.randRectangle() #Does the same thingx as the circle thing except negative
            answer =  getAnswer(currentSet)
            print(answer)
            if answer < WeightMod.discriminator:
                print("The AI incorrectly guessed that this was a circle.")
                WeightMod.adjustWeights(False,  WeightMod.datasetOriginal)
            else:
                print("The AI correctly guessed that this is a rectangle.")
            trainAI(True)
        elif command4 == "init":
            toInit()
    elif not UserInput: #The state in which the user decides if the AI got it right or not
        currentSet = m_data.RandDataset() #43-47 is basically the same as before
        answer =  getAnswer()
        print(answer)
        if answer >= WeightMod.discriminator:
            print("The AI thinks that this is a rectangle. Is this correct?")
            command3 = input("y/n: ")
            if not m_data.YNtoTF(command3): #YNtoTF turns a yes/no input into a boolean
                WeightMod.adjustWeights(True,  WeightMod.datasetOriginal)
            elif command3 == "init":
                toInit()
            trainAI(False)
        else:
            print("The AI thinks that this is a circle. Is this correct?")
            command3 = input("y/n: ")
            if not m_data.YNtoTF(command3): #Just says that if the user says the AI was wrong it needs to be recalibrated
                WeightMod.adjustWeights(False, WeightMod.datasetOriginal)
            trainAI(False)
        

def toInit(): #The init you call at the start of the program, contains all of the starting bits
    print("""
=============================================================
Create PT Python AI 
Commands: 
 "train" to start the manual training process 
 "reset" to reset the AI's weights, essentially resetting the AI(can only be used on this command screen)
 "init" to go to this command screen
""")
    command = input()
    if command == "reset":
        WeightMod.resetWeights(m_data.RandDataset) #Sets all of the weight values to their default 1
        toInit()

    print("==============================================================")
    
    if command == "train":
        print("Would you like to choose whether the AI is shown a circle or square?")
        command2 =  input("y/n: ")
        print("==============================================================")
        trainAI(m_data.YNtoTF(command2))
        if command2 !="y" and command2 != "n":
            toInit()

if __name__ == "__main__":
    toInit()