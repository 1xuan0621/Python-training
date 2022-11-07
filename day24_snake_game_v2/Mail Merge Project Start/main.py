#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Mail Merge Project Start/Input/Names/invited_names.txt') as list:
    invited_list = list.readlines()

new_list = []
for name in invited_list:
    new_list.append(name.strip())

with open('Mail Merge Project Start/Input/Letters/starting_letter.txt') as list:
    content = list.read()

for name in new_list:
    with open(f'Mail Merge Project Start/Output\ReadyToSend/{name}.txt', mode = 'w') as letter:
        new_content = content.replace('[name]', name)
        letter.write(new_content)