import json
import os


# Part one. Take in, edit, save, and create character Jsons

print("Program launched.")

# code to load previously saved or imported characters from the characters folder.
#   This saves the names of the files to a list so that they can be selected from later on.

characterDirectory= os.scandir(path = os.getcwd()+"\characters")

print("character folder confirmed")

numberFilesFound = 0
CharacterFiles = []

with characterDirectory as i:
    for entry in i:
        if entry.is_file():
            numberFilesFound += 1
            CharacterFiles.append(entry.name)

#   1. Aquire the characters folder
#   2. Scan the folder for files, and save their filenames to a list.
#   3. Print out the number of character files located, otherwise state that no files were found.
if numberFilesFound < 1:
    print("No character data located")
else:
    print("Successfully loaded "+str(numberFilesFound)+" characters:")
    for i in CharacterFiles:
        print(i)

print()

currentCharacterData = dict

characterDataVerified = False

while characterDataVerified == False:
    targetCharacterData = input('Please enter the name of the character data file you would like to load: ')
    for i in CharacterFiles:
        if i == targetCharacterData:
            print("Valid character data Located. Importing ... ")
            characterDataVerified = True
            with open('characters/'+targetCharacterData, 'r') as file:
                currentCharacterData = json.load(file)
            break

    if  characterDataVerified == False:
        print("Error: Invalid file name entered. Please ensure you have included the file extension in your response.")

print(currentCharacterData["biography"]["name"])



# to do: Access the data in the characters folder using the list of filenames
#        edit that information through a GUI interface interface
#        Save that edited information back to the file.

# "long term" to do: allow the creation of new character files through terminal
#                    look into Tkinter or some other GUI for python
#                    Add weapons as a property of each character, with those weapons having a create, save, edit function like characters
#                    Add a combat interface that can handle "Roll to hit" / damage rolls using the character and weapon stats.
#                    Add cybernetics