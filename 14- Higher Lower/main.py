import random
import art
import game_data
print(art.logo)
game_on = True
score = 0

while game_on:
    a = random.choice(game_data.data)
    b = random.choice(game_data.data)
    if a == b:
        b = random.choice(game_data.data)
    if a['follower_count'] > b['follower_count']:
        higher_score = 'a'
    else:
        higher_score = 'b'
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")
    awnser = input("Who has more followers? Type 'A' or 'B': ").lower()
    while awnser != 'a' and awnser != 'b':
        awnser = input("Who has more followers? Type ONLY 'A' or 'B': ").lower()
    if awnser == higher_score:
        score += 1
        print(f'You are right, your score is: {score}!')
    else:
        print(f'Sorry, that is wrong. Final score: {score}')
        game_on = False

