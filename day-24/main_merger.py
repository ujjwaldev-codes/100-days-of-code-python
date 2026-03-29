# Mail-Merger to avoid writing mails new for each or to use file handling or automation to also avoid copy paste
with open("./body_of_letter.txt") as file:
    content = file.read()
with open("./list_of_names.txt") as file:
    names = file.readlines()
for name in names:
    name = name.strip()
    with open(f"./bunch_of_letters/letter_to_{name}.txt", mode= "w") as letter:
        letter.write(content.replace("[name]",name))
