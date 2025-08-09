import random

def generate_random_number():
    secret_code = random.randint(1000, 9999)
    return str(secret_code)

def game_setup(code):
    print("Welcome to the Cows and Bulls game!")
    print("You have to guess a 4-digit number.")
    print("For each guess, you will receive feedback on how many digits are correct (cows) and how many are correct but in the wrong position (bulls).")
    print("Let's start the game!")

    while True:
        guessing_number = input("Enter your 4-digit number: ")
        
        if len(guessing_number) != 4 or not guessing_number.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        if guessing_number == code:
                print("Congratulations! You've guessed the number correctly!")
                break
            
        cows = 0
        bulls = 0
        for i in range(len(guessing_number)):
            if guessing_number[i] == code[i]:
                cows +=1
            elif guessing_number[i] in code:
                bulls += 1
        print(f"Cows: {cows}, Bulls: {bulls}")
                
                
def main():
    code = generate_random_number()
    game_setup(code)

main()