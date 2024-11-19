#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

listNames = []
with open('./Input/Names/invited_names.txt') as file:
    content = file.readlines()
    for i in content:
        with open(f"./Input/Letters/starting_letter.txt", mode='r') as f:
            content = f.read()
            name = i.replace('\n', '')
            new_Content = content.replace('[name]', name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='w') as newF:
                contenu = newF.write(new_Content)


