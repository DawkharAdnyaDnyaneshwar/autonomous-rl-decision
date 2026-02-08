import json
from inventory_env import InventoryEnv
from pricing_env import PricingEnv
from q_learning import QLearningAgent

# Inventory training
inv_env = InventoryEnv()
inv_agent = QLearningAgent()

inventory_rewards = []

for episode in range(200):
    state = inv_env.reset()
    total = 0
    for _ in range(50):
        action = inv_agent.act(state)
        next_state, reward = inv_env.step(action)
        inv_agent.update(state, action, reward, next_state)
        state = next_state
        total += reward
    inventory_rewards.append(total)

# Pricing training
price_env = PricingEnv()
price_agent = QLearningAgent(states=30, actions=3)

pricing_rewards = []
price_history = []

for episode in range(200):
    state = price_env.reset()
    total = 0
    for _ in range(50):
        action = price_agent.act(state) - 1  # -1,0,+1
        next_state, reward = price_env.step(action)
        price_agent.update(state, action+1, reward, next_state)
        state = next_state
        total += reward
    pricing_rewards.append(total)
    price_history.append(state)

output = {
    "inventory_rewards": inventory_rewards,
    "pricing_rewards": pricing_rewards,
    "price_history": price_history
}

print(json.dumps(output))
