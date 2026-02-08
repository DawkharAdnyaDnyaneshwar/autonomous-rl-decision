const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");

const app = express();
app.use(cors());

app.get("/train", (req, res) => {
    const python = spawn("python", ["../rl_engine/train.py"]);

    let data = "";

    python.stdout.on("data", (chunk) => {
        data += chunk.toString();
    });

    python.on("close", () => {
        try {
            res.json(JSON.parse(data));
        } catch (err) {
            res.status(500).send("Training error");
        }
    });
});

app.listen(5000, () => {
    console.log("Server running on port 5000");
});
