PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names:
    invited_names = names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letter_content = letter.read()
    for name in invited_names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)

