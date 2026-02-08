import random

class PricingEnv:
    def __init__(self):
        self.base_demand = 50
        self.reset()

    def reset(self):
        self.price = 10
        return self.price

    def step(self, action):
        # action: -1, 0, +1 price change
        self.price += action
        self.price = max(5, min(self.price, 20))

        # demand decreases as price increases
        demand = int(self.base_demand - self.price * random.uniform(1.5, 2.5))
        demand = max(0, demand)

        revenue = self.price * demand
        reward = revenue

        return self.price, reward
