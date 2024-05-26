import random
computer_num = random.randint(0, 4096)
while True:
    guess = int(input("Give number: "))
    if guess > computer_num:
        print("Too high")
    elif guess < computer_num:
        print("To low")
    elif guess == computer_num:
        print("Congratulations! You guessed the number!")
        play_again = input("Want to play again? (Y/N): ")
        if play_again.upper() == 'Y':
            computer_num = random.randint(0, 4096)
        else:
            break
print("Game ended")