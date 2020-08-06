import random


def score_draw(score):
    return score + 50


def score_win(score):
    return score + 100


name = input("Enter your name:")
print("Hello, " + name)

file = open("rating.txt", "r")
for line in file:
    parts = line.split()
    name_part = parts[0]
    if name_part == name:
        score = int(parts[1])
        break
    else:
        score = 0
print(name, score)

while True:
    user_input = input()
    computer_input = {0: "paper", 1: "rock", 2: "scissors"}
    number = random.randint(0, 2)
    if user_input == "rock":
        if number == 0:
            print("Sorry, but computer chose " + computer_input[number])
        elif number == 1:
            print("There is a draw (" + computer_input[number] + ")")
            score = score_draw(score)
        elif number == 2:
            print("Well done. Computer chose " + computer_input[number] + " and failed")
            score = score_win(score)

    elif user_input == "paper":
        if number == 2:
            print("Sorry, but computer chose " + computer_input[number])
        elif number == 0:
            print("There is a draw (" + computer_input[number] + ")")
            score = score_draw(score)
        elif number == 1:
            print("Well done. Computer chose " + computer_input[number] + " and failed")
            score = score_win(score)
    elif user_input == "scissors":
        if number == 1:
            print("Sorry, but computer chose " + computer_input[number])
        elif number == 2:
            print("There is a draw (" + computer_input[number] + ")")
            score = score_draw(score)
        elif number == 0:
            print("Well done. Computer chose " + computer_input[number] + " and failed")
            score = score_win(score)
    elif user_input == "!rating":
        print("Your rating: " + str(score))
    elif user_input == "!exit":
        print("Bye!")
        break
    else:
        print("Invalid input")