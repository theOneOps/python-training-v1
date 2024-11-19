#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

list_invitation = []

with open("./Input/Names/invited_names.txt") as names_files:
    list_names = names_files.readlines()
    for i in list_names:
        change_name = i.replace('\n', "")
        list_invitation.append(change_name)
    print(list_invitation)

with open("./Input/Letters/starting_letter.txt") as text_message:
    content_message = text_message.read()
    for i in list_invitation:
        example = content_message.replace("[name],", f"{i},")
        print(example)
        with open(f"./Output/ReadyToSend/example_{i}.txt", mode='w') as completed_message :
            completed_message.write(example)



