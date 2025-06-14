import random
from ai_ml import predictor, train_ai, move_to_number


def random_move():
    return random.choice(['rock', 'paper', 'scissors'])


def rule_based_move(player_moves):
    if len(player_moves) >= 2:
        if player_moves[-1] == player_moves[-2]:
            if player_moves[-1] == 'rock':
                return 'paper'
            elif player_moves[-1] == 'paper':
                return 'scissors'
            else:
                return 'rock'
    return random_move()


def ai_move(player_moves):
    train_ai(player_moves)

    if predictor.is_fitted and len(player_moves) >= 3:
        input_seq = [move_to_number(move) for move in player_moves[-3:]]
        predicted_move = predictor.predict_move(player_moves)
        prediction_prob = max(predictor.model.predict_proba([input_seq])[0])
    else:
        predicted_move = random_move()
        prediction_prob = 0

    trust_threshold = 0.6

    if prediction_prob > trust_threshold:
        return predicted_move
    else:
        random_decision = random_move()
        rule_based_decision = rule_based_move(player_moves)

        decisions = [random_decision, rule_based_decision, predicted_move]
        weights = [0.2, 0.3, prediction_prob]

        return random.choices(decisions, weights=weights, k=1)[0]