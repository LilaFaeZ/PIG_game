import random

def one_player():
    turn_total = 0
    faces = [1, 2, 3, 4, 5, 6]
    score = 0
    valid = False
    while not valid:
        result = random.choice(faces)
        print("Roll:", result)
        if result == 1:
            turn_total = 0
            print("Turn total:", turn_total)
            print("New score:", score)
        if result != 1:
            turn_total += result
            if score + turn_total > 99:
                score += turn_total
                print("Turn total:", turn_total)
                valid = True
            elif turn_total >= 20:
                print("Turn total:", turn_total)
                score += turn_total
                print("New Score:", score)
                turn_total = 0 #initialize the turn total AFTER adding to score
    return score
print("New Score:", one_player())

"""
What my goal is:
1. create a solo playing game of PIG
2. create turns where there are THREE conditions
    1. if a roll in a turn is 1, the entire turn total is 0
    2. if all the rolls never equal 1 and a turn is 20 or greater (25 at most), then that turn
    will be added to the score
    3. if the score reaches 100 from the turn total, then the turn is cut short regardless 
    of if the turn reached to 20 or not. (for example, score starts at 90, if the turn is one
    roll of 6, then 3, then 4, it would stop because the score is 103, even if the turn is 
    only equal to 13.)
"""