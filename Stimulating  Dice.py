
# DICE STIMULATOR
import random
def roll_dice():
    return random.randint(1,6)
    
def main():
    print("Welcome to the Dice Stimulator")
    while True:
        input_text = input("Press Enter to roll the dice or type Quit to exit").strip().lower()
        if input_text=='quit':
            print("Thank You for using the dice stimulator.Goodbye!")
            break
        else:
            result = roll_dice()
            print(f'You rolled {result}!')
            print()
            
if __name__=="__main__":
    main()

#CUSTOMIZATION 1

import random as anmol

while True:
    try:
        Rahul = int(input("Enter the no. of players"))
        if Rahul == 4:
            a=[]
            b=[]
            c=[]
            d=[]
            e=0
            f=0
            g=0
            h=0
        
            Player1=input("Please Enter the first Player Name --> ")
            Player2=input("Please Enter the Second Player Name --> ")
            Player3=input("Please Enter the Third Player Name --> ")
            Player4=input("Please Enter the Fourth Player Name --> ")
    
            for i in range(10):
                p=anmol.randint(1,6)
                m=anmol.randint(1,6)
                n=anmol.randint(1,6)
                o=anmol.randint(1,6)
                
                a.append(p)
                b.append(m)
                c.append(n)
                d.append(o)
                
                e += p
                f += m
                g += n
                h += o 
    
    
                print(Player1,"list of score",a)
                print(Player2,"list of score",b)
                print(Player3,"list of score",c)
                print(Player4,"list of score",d)
    
                print(Player1,"Score is",e)
                print(Player2,"Score is",f)
                print(Player3,"Score is",g)
                print(Player4,"Score is",h)
    
            if e>f and e>g and e>h :
                print("Winner of the game is ",Player1)
            elif f>e and f>g and f>h :
                print("Winner of the game is ",Player2)
            elif g>e and g>g and g>h:
                print("Winner of the game is ",Player3)
            elif h>e and h>f and h>g:
                print("Winner of the game is ",Player4)
            break
    
    except keyerror:
        print('enter any integer please')
    except zeroDivisionError:
        print('cant divide by zero')
    finally:
        print("Thanks for Playing the Game")

# CUSTOMIZATION 2

import random

def simulate_dice_roll(target_number, total_rolls):
    rolls = [random.randint(1, 6) for _ in range(total_rolls)]
    target_count = rolls.count(target_number)
    return rolls, target_count

def main():
    target_number = int(input("Enter the target number (1 to 6): "))
    total_rolls = int(input("Enter the total number of rolls: "))

    rolls, target_count = simulate_dice_roll(target_number, total_rolls)

    print("Dice Rolls:", rolls)
    print(f"Number of times {target_number} appeared:", target_count)

if __name__ == "__main__":
    main()

#Customizatin 3

import random

def simulate_dice_roll():
    return random.randint(1, 6)

def main():
    players = {
        "Anmol Sharma": 0,
        "Rahul Sharma": 0,
        "Kashii Sharma": 0,
        "Vivek Sharma": 0
    }

    target_player = input("Enter the player name you want to win: ")
    target_numbers = [int(x) for x in input("Enter the targeted numbers for winning (comma-separated): ").split(",")]

    rolls_count = 10  # Number of rolls per player

    for player in players:
        for _ in range(rolls_count):
            roll = simulate_dice_roll()
            print(f"{player} rolls:", roll)
            if player == target_player and roll in target_numbers:
                players[player] += 1

    winner = max(players, key=players.get)
    print(f"\nWinner of the game is {winner}")

if __name__ == "__main__":
    main()
    
#Customizatin 4

import random
def simulate_dice_roll():
    return random.randint(1, 6)

def main():
    players = {
        "Player1": {"score": 0, "target_count": 0},
        "Player2": {"score": 0, "target_count": 0},
        "Player3": {"score": 0, "target_count": 0},
        "Player4": {"score": 0, "target_count": 0}
    }

    target_player = input("Enter the player name you want to win: ")
    target_numbers = [int(x) for x in input("Enter the targeted numbers for winning (comma-separated): ").split(",")]

    rolls_count = 10  # Number of rolls per player

    for player in players:
        for _ in range(rolls_count):
            roll = simulate_dice_roll()
            print(f"{player} rolls:", roll)
            if roll in target_numbers:
                players[player]["score"] += 1
                if player == target_player:
                    players[player]["target_count"] += 1

    winner = max(players, key=lambda x: (players[x]["score"], players[x]["target_count"]))
    total_score = sum(players[player]["score"] for player in players)
    total_target_count = sum(players[player]["target_count"] for player in players)

    print("\nIndividual Player Scores:")
    for player, data in players.items():
        print(f"{player}: Score - {data['score']}, Target Count - {data['target_count']}")

    print("\nTotal Score for All Players:", total_score)
    print("Total Target Count:", total_target_count)
    print(f"\nWinner of the game is {winner}")

if __name__ == "__main__":
    main()

#customizatin 5

import random
def simulate_dice_roll():
    return random.randint(1, 6)

def main():
    players = {
        "Anmol Sharma": {"score": [], "target_count": 0},
        "Rahul Sharma": {"score": [], "target_count": 0},
        "Kashii Sharma": {"score": [], "target_count": 0},
        "Vivek Sharma": {"score": [], "target_count": 0}
    }

    target_player = input("Enter the player name you want to win: ")
    target_numbers = [int(x) for x in input("Enter the targeted numbers for winning (comma-separated): ").split(",")]

    rolls_count = 10  # Number of rolls per player

    for player in players:
        for _ in range(rolls_count):
            roll = simulate_dice_roll()
            print(f"{player} rolls:", roll)
            players[player]["score"].append(roll)
            if roll in target_numbers:
                players[player]["target_count"] += 1

    total_score = sum(sum(player_data["score"]) for player_data in players.values())
    print("\nIndividual Player Scores and Total Score:")
    for player, data in players.items():
        individual_score = sum(data["score"])
        print(f"{player}: Scores - {data['score']}, Total Score - {individual_score}, Target Count - {data['target_count']}")
    
    print("\nTotal Score for All Players:", total_score)

    winner = max(players, key=lambda x: (sum(players[x]["score"]), players[x]["target_count"]))
    print(f"\nWinner of the game is {winner}")

if __name__ == "__main__":
    main()
    
#Customization 6 

import random
def simulate_dice_roll():
    return random.randint(1, 6)

def main():
    players = {
        "Anmol Sharma": {"score": [], "target_count": 0},
        "Rahul Sharma": {"score": [], "target_count": 0},
        "Kashii Sharma": {"score": [], "target_count": 0},
        "Vivek Sharma": {"score": [], "target_count": 0}
    }

    target_player = input("Enter the player name you want to win: ")
    target_numbers = [int(x) for x in input("Enter the targeted numbers for winning (comma-separated): ").split(",")]

    rolls_count = 10  # Number of rolls per player

    for player in players:
        for _ in range(rolls_count):
            roll = simulate_dice_roll()
            print(f"{player} rolls:", roll)
            players[player]["score"].append(roll)
            if roll in target_numbers:
                players[player]["target_count"] += 1

    total_score = sum(sum(player_data["score"]) for player_data in players.values())
    print("\nIndividual Player Scores and Total Score:")
    sorted_players = sorted(players.items(), key=lambda x: sum(x[1]["score"]), reverse=True)
    for i, (player, data) in enumerate(sorted_players):
        individual_score = sum(data["score"])
        if i == 0:
            tag = "👑 1st"
        elif i == 1:
            tag = "🥈 2nd"
        elif i == 2:
            tag = "🥉 3rd"
        else:
            tag = "👎 Loser"
        print(f"{player}: Scores - {data['score']}, Total Score - {individual_score}, Target Count - {data['target_count']}, {tag}")
    
    print("\nTotal Score for All Players:", total_score)

    winner = sorted_players[0][0]
    print(f"\nWinner of the game is {winner} 👑")

if __name__ == "__main__":
    main()
