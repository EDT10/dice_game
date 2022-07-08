import random

high_score = 0

def dice_game():
    while True:
        # was reluctant to do use the keyword global here but this is the only way i could figure out without getting error
        global high_score

        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print("You roll a...", dice1)
            print("You roll a...", dice2, "\n")

            total = dice1 + dice2
            print("You have rolled a total of:", total, "\n")
            if total > high_score:
                print("NEW HIGH SCORE!!\n")
                high_score = total
            print("Current high score: ", high_score, "\n")
        else:
            print("Goodbye!")
            quit()

dice_game()
