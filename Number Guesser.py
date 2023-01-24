from random import randint


def is_valid(number):
    return 1 <= number <= int(n)


def game():
    global n
    global player_answer
    print('Please enter n (number limit). Number must be an integer more than 1')
    n = input()
    while not n.isdigit():
        print('Please enter a valid integer number more than 1')
        n = input()
    while int(n) <= 2 and int(n) % 1 != 0:
        print('Please enter a valid integer number more than 1')
        n = input()
    random_number = randint(1, int(n))
    counter = 1
    print('Enter a number from 1 to', n)
    user_number = input()
    while not user_number == str(random_number):
        if not user_number.isdigit():
            print('Please enter a valid integer number from 1 to', n)
            user_number = input()
        else:
            if not is_valid(int(user_number)):
                print('Please enter a valid number from 1 to', n)
                user_number = input()
            else:
                if int(user_number) < random_number:
                    print('Your number is less than expected, please try again')
                    user_number = input()
                    counter += 1
                elif int(user_number) > random_number:
                    print('Your number is higher than expected, please try again')
                    user_number = input()
                    counter += 1
    if int(user_number) == random_number:
        print('You guessed it on the', counter, 'try, congratulations!')
        print('Do you want to play one more time? Enter "yes" or "no".')
        player_answer = input()


def restart():
    global player_answer
    while True:
        if player_answer.lower() == 'no':
            print('Thanks for playing the number guessing game. See you...')
            break
        elif player_answer.lower() == 'yes':
            game()
        else:
            print('Please enter the correct answer: "yes" or "no"')
            player_answer = input()


print('Welcome to the Number Guesser')
print('We will play a game with you in which you will need to guess a hidden number from 1 to n.')
game()
restart()
