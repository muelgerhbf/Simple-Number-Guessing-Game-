import random

print(
    "Welcome to Number guessing game in Python!\n" "Type which range you want to play: "
)

low = int(input("Your lowest number: "))
high = int(input("Your highest number: "))

print(f"L:{low}\nH:{high}")


def random_number_generator(low, high):
    return random.randint(low, high)


target_number = random_number_generator(low, high)

# print(random_number_generator(low, high))   | this only works if low and high variables   |
#                                             | are returning int and not strings           |
#                                             | i_value = int(input(""))                    |

guess_number_id = 1
user_guess_input = int(input(f"Guess {guess_number_id}: "))

while user_guess_input != target_number:
    guess_number_id += 1
    print("false. Try again")
    user_guess_input = int(input(f"Guess {guess_number_id}: "))
    if target_number > user_guess_input:
        print("Your number is too low baby")
    elif target_number < user_guess_input:
        print("Your number is too high baby")
    else:
        print(f"You got it babygirl.\nTarget: {target_number}")
