import React, { useState } from "react";
import { Line } from "react-chartjs-2";
import "chart.js/auto";
import "./App.css";

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const trainAgent = async () => {
    setLoading(true);
    const res = await fetch("https://rl-backend-3ndj.onrender.com/train");
    const result = await res.json();
    setData(result);
    setLoading(false);
  };

  return (
    <div className="container">
      <header className="header">
        <h1>Autonomous RL Decision Dashboard</h1>
        <button className="train-btn" onClick={trainAgent}>
          {loading ? "Training..." : "Train Agent"}
        </button>
      </header>

      {data && (
        <div className="grid">
          {/* Inventory Chart */}
          <div className="card">
            <h2>Inventory Learning Curve</h2>
            <Line
              data={{
                labels: data.inventory_rewards.map((_, i) => i),
                datasets: [
                  {
                    label: "Inventory Reward",
                    data: data.inventory_rewards,
                  },
                ],
              }}
            />
          </div>

          {/* Pricing Chart */}
          <div className="card">
            <h2>Pricing Learning Curve</h2>
            <Line
              data={{
                labels: data.pricing_rewards.map((_, i) => i),
                datasets: [
                  {
                    label: "Pricing Reward",
                    data: data.pricing_rewards,
                  },
                ],
              }}
            />
          </div>

          {/* Price Trend */}
          <div className="card">
            <h2>Price Trend</h2>
            <Line
              data={{
                labels: data.price_history.map((_, i) => i),
                datasets: [
                  {
                    label: "Selected Price",
                    data: data.price_history,
                  },
                ],
              }}
            />
          </div>

          {/* Model Insights */}
          <div className="card">
            <h2>Model Insights</h2>
            <ul className="insights">
              <li><strong>Algorithm:</strong> Q-Learning (from scratch)</li>
              <li><strong>Inventory State:</strong> Current stock level</li>
              <li><strong>Pricing State:</strong> Current price</li>
              <li><strong>Actions:</strong> Restock or price adjustment</li>
              <li><strong>Reward:</strong> Profit-based optimization</li>
              <li><strong>Goal:</strong> Maximize long-term cumulative reward</li>
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
