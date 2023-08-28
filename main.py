import random

def main():
    horses = generate_horses(5)
    print("Welcome to the Horse Track!")
    print_horses(horses)
    
    player_choice = get_player_choice(horses)
    
    if player_choice is not None:
        bet_amount = get_bet_amount()
        play_race(horses, player_choice, bet_amount)

def generate_horses(num_horses):
    funny_names = [
        "Sir Galloping Giggles",
        "Mystical Mane Master",
        "Captain Thunderhooves",
        "Duchess of Dashing",
        "Spectacular Speedy Spots"
    ]
    random.shuffle(funny_names)  # Shuffle the list of horse names
    horses = []
    for i in range(num_horses):
        horse_name = funny_names[i]
        odds = random.uniform(2.0, 5.0)  # Generate random odds between 2.0 and 5.0
        horses.append((horse_name, odds))
    return horses

def print_horses(horses):
    print("Horse List:")
    for i, (horse_name, odds) in enumerate(horses, start=1):
        print(f"{i}. {horse_name} - Odds: {odds:.2f}")

def get_player_choice(horses):
    num_horses = len(horses)
    while True:
        try:
            choice = int(input(f"Choose a horse (1-{num_horses}): "))
            if 1 <= choice <= num_horses:
                return choice - 1  # Adjust index to match list indexing
            else:
                print("Invalid choice. Please select a valid horse.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_bet_amount():
    while True:
        try:
            bet_amount = float(input("Enter your bet amount: "))
            if bet_amount > 0:
                return bet_amount
            else:
                print("Invalid bet amount. Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_race(horses, player_choice, bet_amount):
    winner = random.choice(horses)
    print("\nThe race is on!")
    print(f"The winner is... {winner[0]}!")

    if winner == horses[player_choice]:
        winnings = bet_amount * horses[player_choice][1]
        print(f"Congratulations! You've won {winnings:.2f}!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()




