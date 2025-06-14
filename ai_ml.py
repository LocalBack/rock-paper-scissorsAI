from sklearn.linear_model import LogisticRegression
import numpy as np
import random

class MovePredictor:
    def __init__(self):
        self.model = LogisticRegression()
        self.data = []
        self.labels = []
        self.is_fitted = False

    def add_data(self, sequence, outcome):
        if len(sequence) == 3:  # Ensure sequence is of the expected length
            self.data.append(sequence)
            self.labels.append(outcome)

    def fit_model(self):
        if len(self.data) > 3:  # Ensure enough data
            X = np.array(self.data)
            y = np.array(self.labels)
            self.model.fit(X, y)
            self.is_fitted = True

    def predict_move(self, recent_moves):
        if self.is_fitted and len(recent_moves) >= 3:
            input_seq = [move_to_number(move) for move in recent_moves[-3:]]
            return number_to_move(self.model.predict([input_seq])[0])
        else:
            return random.choice(['rock', 'paper', 'scissors'])

def move_to_number(move):
    return {'rock': 0, 'paper': 1, 'scissors': 2}[move]

def number_to_move(number):
    return {0: 'rock', 1: 'paper', 2: 'scissors'}[number]

# Initialize predictor globally to persist data across games
predictor = MovePredictor()

def train_ai(player_moves):
    if len(player_moves) >= 4:  # Ensure there are enough moves to make a prediction
        sequence = [move_to_number(m) for m in player_moves[-4:-1]]  # Last 3 moves
        outcome = move_to_number(player_moves[-1])
        predictor.add_data(sequence, outcome)
        predictor.fit_model()