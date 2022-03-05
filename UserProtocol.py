import gc
from typing import final
gc.disable()
from WeightMod import adjustWeights, applyWeights, concatenateWeights, discriminator
from DatasetManager import RandDataset, YNtoTF

command = ""
currentSet = []
finalAnswer = ""

def toInit():
    print('=============================================================\nCreate PT Python AI \nCommands: \n "train" to start the manual training process \n "weights" to view the AI\'s weights\n "reset" to reset the AI\'s weights')
    command = input()
    print("==============================================================")
    
    if command == "train":
        print("Would you like to choose whether the AI is shown a circle or square?")
        command2 =  input("y/n: ")
        print("==============================================================")
        trainAI(YNtoTF(command2))
        if command2 !="y" and command2 != "n":
            toInit()

toInit()

def trainAI( UserInput):
    global finalAnswer
    if UserInput:
        ""
    else:
        currentSet = RandDataset()
        applyWeights(currentSet)
        finalAnswer = concatenateWeights(currentSet)
        if finalAnswer >= discriminator:
            print("The AI thinks that this is a rectangle. Is this correct?")
            command3 = input("y/n: ")
            if YNtoTF(command3) == False:
                adjustWeights(True)
            #add weight viewer stuff here
        elif finalAnswer < discriminator:
            print("The AI thinks that this is a circle. Is this correct?")
            command3 = input("y/n: ")
            if YNtoTF(command3) == False:
                adjustWeights(False)
            #and here
        
        


        

        

# if command == "train":
#     print("Would you like to choose whether the AI is shown a circle or square?")
#     command2 =  input("y/n: ")
#     print("==============================================================")
#     trainAI()

