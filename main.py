import random
import art
import words

chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(art.logo)

#print(f'The solution is {chosen_word}.') #TESTING CODE

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"{guess} already in word")

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") #debugging code
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(art.stages[lives])