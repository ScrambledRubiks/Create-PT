
import WeightMod
import DatasetManager

command = ""
currentSet = []
finalAnswer = ""


def trainAI(UserInput):
    global finalAnswer
    global currentSet
    if UserInput:
        print("Should the AI be shown a circle or a rectangle?")
        command4 = input("c/r: ")
        if command4 == "c":
            currentSet = DatasetManager.data.randCircle()
            DatasetManager.data.DisplayDataset(currentSet)
            WeightMod.datasetOriginal = currentSet
            WeightMod.applyWeights(currentSet)
            finalAnswer = WeightMod.concatenateWeights(currentSet)
            if finalAnswer >= WeightMod.discriminator:
                print("The AI incorrectly guessed that this was a rectangle.")
                WeightMod.adjustWeights(True,  WeightMod.datasetOriginal)
            else:
                print("The AI correctly guessed that this is a circle.")
            trainAI(True)
        elif command4 == "r":
            currentSet = DatasetManager.data.randRectangle()
            DatasetManager.data.DisplayDataset(currentSet)
            WeightMod.datasetOriginal = currentSet
            WeightMod.applyWeights(currentSet)
            finalAnswer = WeightMod.concatenateWeights(currentSet)
            if finalAnswer < WeightMod.discriminator:
                print("The AI incorrectly guessed that this was a circle.")
                WeightMod.adjustWeights(False,  WeightMod.datasetOriginal)
            else:
                print("The AI correctly guessed that this is a rectangle.")
            trainAI(True)
        elif command4 == "init":
            toInit()
    elif not UserInput:
        currentSet = DatasetManager.data.RandDataset()
        DatasetManager.data.DisplayDataset(currentSet)
        WeightMod.datasetOriginal = currentSet
        WeightMod.applyWeights(currentSet)
        finalAnswer = WeightMod.concatenateWeights(currentSet)
        
        
        if finalAnswer >= WeightMod.discriminator:
            print("The AI thinks that this is a rectangle. Is this correct?")
            command3 = input("y/n: ")
            if DatasetManager.data.YNtoTF(command3) == False:
                WeightMod.adjustWeights(True,  WeightMod.datasetOriginal)
            elif command3 == "init":
                toInit()
            elif command3 == "init":
                toInit()
            #add weight viewer stuff here
            trainAI(False)
        elif finalAnswer < WeightMod.discriminator:
            print("The AI thinks that this is a circle. Is this correct?")
            command3 = input("y/n: ")
            if not DatasetManager.data.YNtoTF(command3):
                WeightMod.adjustWeights(False, WeightMod.datasetOriginal)
            trainAI(False)
        

def toInit():
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
        WeightMod.resetWeights()
        toInit()

    print("==============================================================")
    
    if command == "train":
        print("Would you like to choose whether the AI is shown a circle or square?")
        command2 =  input("y/n: ")
        print("==============================================================")
        trainAI(DatasetManager.data.YNtoTF(command2))
        if command2 !="y" and command2 != "n":
            toInit()

toInit()