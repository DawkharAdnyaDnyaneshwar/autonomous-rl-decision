import random

class InventoryEnv:
    def __init__(self):
        self.max_inventory = 100
        self.reset()

    def reset(self):
        self.inventory = 50
        return self.inventory

    def step(self, action):
        demand = random.randint(5, 20)

        # restock
        self.inventory += action
        self.inventory = min(self.inventory, self.max_inventory)

        sales = min(self.inventory, demand)
        self.inventory -= sales

        profit = sales * 20
        holding_cost = self.inventory * 2
        stockout_penalty = 50 if self.inventory == 0 else 0

        reward = profit - holding_cost - stockout_penalty
        return self.inventory, reward
