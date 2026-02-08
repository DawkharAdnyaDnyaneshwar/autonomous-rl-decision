import random

class QLearningAgent:
    def __init__(self, states=101, actions=20):
        self.q = [[0 for _ in range(actions)] for _ in range(states)]
        self.lr = 0.1
        self.gamma = 0.95
        self.epsilon = 0.1
        self.actions = actions

    def act(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.actions - 1)
        return self.q[state].index(max(self.q[state]))

    def update(self, s, a, r, s_next):
        best_next = max(self.q[s_next])
        self.q[s][a] += self.lr * (
            r + self.gamma * best_next - self.q[s][a]
        )
