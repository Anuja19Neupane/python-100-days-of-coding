PLACEHOLDER = "[name]"

with open("day_24/invited_names.txt") as file:
    names = file.readlines()  # readlines le list ma convert garxa
    # print(names)

with open("day_24/starting_letters.txt") as newfile:
    letters = newfile.read()
    for name in names:
        stripped_name = name.strip()  # strip le side ko space harlai cancel garxa
        new_letter = letters.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"ready_to_send/letter_for{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
