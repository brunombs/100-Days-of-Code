from random import randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('Welcome to rock, paper and scissors.')
choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: '))
computer = randint(0,2)
choice_list = [rock, paper, scissors]

if choice >= 3 or choice <= 0:
    print('Invalid number, you lose.')
else:
    if choice == computer:
        print('That is a draw.')
    elif choice == 0 and computer == 1:
        print('You lose')
    elif choice == 0 and computer == 2:
        print('You win.')
    elif choice == 1 and computer == 0:
        print('You lose.')
    elif choice == 1 and computer == 2:
        print('You lose.')
    elif choice == 2 and computer == 0:
        print('You lose.')
    elif choice == 2 and computer == 1:
        print('You win.')

print(f'You chose: {choice_list[computer]}')
print(f'Computer chose: {choice_list[computer]}')
