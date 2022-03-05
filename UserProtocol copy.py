
import WeightMod
import DatasetManager

command = ""
currentSet = []
finalAnswer = ""

def trainAI( UserInput):
    global finalAnswer
    if UserInput:
        ""
    else:
        currentSet = DatasetManager.data.RandDataset()
        WeightMod.applyWeights(currentSet)
        finalAnswer = WeightMod.concatenateWeights(currentSet)
        if finalAnswer >= WeightMod.discriminator:
            print("The AI thinks that this is a rectangle. Is this correct?")
            command3 = input("y/n: ")
            if DatasetManager.data.YNtoTF(command3) == False:
                WeightMod.adjustWeights(True,  currentSet)
            #add weight viewer stuff here
            trainAI(False)
        elif finalAnswer < WeightMod.discriminator:
            print("The AI thinks that this is a circle. Is this correct?")
            command3 = input("y/n: ")
            if not DatasetManager.data.YNtoTF(command3):
                WeightMod.adjustWeights(False, currentSet)
            trainAI(False)
            #and here

def toInit():
    print("""
=============================================================
Create PT Python AI 
Commands: 
 "train" to start the manual training process 
 "weights" to view the AI's weights
 "reset" to reset the AI's weights
""")
    command = input()
    print("==============================================================")
    
    if command == "train":
        print("Would you like to choose whether the AI is shown a circle or square?")
        command2 =  input("y/n: ")
        print("==============================================================")
        trainAI(DatasetManager.data.YNtoTF(command2))
        if command2 !="y" and command2 != "n":
            toInit()

toInit()

        
        


        

        

# if command == "train":
#     print("Would you like to choose whether the AI is shown a circle or square?")
#     command2 =  input("y/n: ")
#     print("==============================================================")
#     trainAI()

