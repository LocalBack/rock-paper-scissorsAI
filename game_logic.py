def determine_winner(player, ai):
    if player == ai:
        return "It's a draw!"
    elif (player == 'rock' and ai == 'scissors') or \
         (player == 'scissors' and ai == 'paper') or \
         (player == 'paper' and ai == 'rock'):
        return "You win!"
    else:
        return "AI wins!"