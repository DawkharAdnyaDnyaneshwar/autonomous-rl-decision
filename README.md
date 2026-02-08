Autonomous Decision-Making System using Reinforcement Learning
Overview

This project implements a full-stack autonomous decision system that learns optimal strategies for inventory restocking and dynamic pricing using Reinforcement Learning (RL).

The system models business decision problems as Markov Decision Processes (MDPs) and trains agents using Q-Learning implemented from scratch, without using any RL frameworks or deep learning libraries.

A Node.js backend connects the Python RL engine to a React dashboard, allowing real-time training and visualization of the agent’s performance.

🌐 Live Demo

Frontend Dashboard:
https://rl-decision.netlify.app/

Backend API:
https://rl-backend-3ndj.onrender.com/train

Problem Statement

Traditional rule-based systems for inventory and pricing:

Cannot adapt to changing demand

Focus only on short-term profit

Fail under uncertain environments

This project builds an autonomous agent that:

Learns from interaction with the environment

Makes sequential decisions

Maximizes long-term cumulative profit

Key Features

Inventory restocking optimization

Dynamic pricing based on demand elasticity

Reinforcement Learning implemented from scratch

No Gym, no PyTorch, no deep learning frameworks

Node.js backend to execute RL training

React dashboard for visual analytics

Real-time learning curves and model insights

System Architecture
React Frontend (Dashboard)
        |
        v
Node.js Express API
        |
        v
Python RL Engine (Q-Learning from scratch)

How the System Works

User opens the dashboard.

User clicks Train Agent.

Frontend sends a request to the Node.js backend.

Backend executes the Python RL training script.

The RL agent interacts with the environment and learns.

Training results are returned as JSON.

Dashboard displays learning curves and insights.

Reinforcement Learning Formulation
Inventory Optimization

State:

Current inventory level

Action:

Restock quantity

Reward:

profit − holding_cost − stockout_penalty

Pricing Optimization

State:

Current product price

Action:

Increase price

Decrease price

Keep price same

Reward:

price × demand

Goal

Maximize long-term cumulative reward.

Algorithm Used

Q-Learning (implemented from scratch)

ε-greedy exploration strategy

Tabular value function

Tech Stack
Frontend

React

Chart.js

CSS

Backend

Node.js

Express

AI Engine

Python

Custom RL environments

Q-Learning implementation

Project Structure
rl-decision-system/
│
├── backend/
│   ├── server.js
│   └── package.json
│
├── rl_engine/
│   ├── inventory_env.py
│   ├── pricing_env.py
│   ├── q_learning.py
│   └── train.py
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
│
└── README.md

Dashboard Features

After clicking Train Agent, the dashboard shows:

1. Inventory Learning Curve

Reward vs episode

Shows improvement over time

2. Pricing Learning Curve

Revenue optimization trend

3. Price Trend

How the agent adjusts prices

4. Model Insights

Algorithm used

State and action definitions

Reward logic

Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/rl-decision-system.git
cd rl-decision-system

2. Start Backend
cd backend
npm install
node index.js


Backend runs on:

http://localhost:5000

3. Start Frontend

Open a new terminal:

cd frontend
npm install
npm start


Frontend runs on:

http://localhost:3000

API Endpoint
Train RL Agent
GET /train

Example Response
{
  "inventory_rewards": [1200, 1400, 1600, ...],
  "pricing_rewards": [800, 950, 1100, ...],
  "price_history": [10, 11, 12, ...]
}

Sample Results

Reduced inventory stockouts

Improved long-term profit

Learned stable pricing strategy

Converging reward curves over episodes

Deployment

Frontend: Netlify

Backend: Render

Live links:

Frontend: https://rl-decision.netlify.app/
Backend: https://rl-backend-3ndj.onrender.com/train