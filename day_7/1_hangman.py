# have some problem here
# word_list ma vako word user le namilaun jel samma run hunuparney code.
import random
word_list = ["giby", "kiwi", "you"]
choosen_word = random.choice(word_list)
# print(choosen_word)
print(f"THERE ARE {len(choosen_word)} LETTERS")
display = []
for letter in choosen_word:
    display += "_"
print(display)
end_of_game = False
lives = 6
while not end_of_game:

    guess = input("guess a letter: ").lower()
#[ print(guess)]
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
    # for letter in choosen_word:
        if letter == guess:
            display[position] = letter
# if guess is not a letter in the choosen_word,
 # then reduce 'lives' by 1.
# if lives goes down to 0 then the game should stop and
# it should print "you loose."

    if guess not in choosen_word:
        lives -= 1
    print(f"YOU HAVE {lives} lives left")
    if lives == 0:
        end_of_game = True
        print("you loose")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("YOU WIN")
