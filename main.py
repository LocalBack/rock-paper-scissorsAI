from ai import ai_move
from game_logic import determine_winner


def main():
    player_moves = []
    ai_score = 0
    user_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play ('r', 'p', 's' for short). Type 'exit' to quit.")

    while True:
        player_choice = input("Enter your move: ").lower()

        if player_choice == 'exit':
            print("Thanks for playing!")
            break

        # Map shorthand inputs to full words
        if player_choice in ['r', 'p', 's']:
            player_choice = {'r': 'rock', 'p': 'paper', 's': 'scissors'}[player_choice]

        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid move! Please try again.")
            continue

        player_moves.append(player_choice)
        ai_choice = ai_move(player_moves)
        print(f"AI chose: {ai_choice}")

        result = determine_winner(player_choice, ai_choice)
        print(result)

        # Update scores
        if "AI wins" in result:
            ai_score += 1
        elif "You win" in result:
            user_score += 1

        # Display current scores
        print(f"AI : {ai_score}   User : {user_score}")


if __name__ == "__main__":
    main()