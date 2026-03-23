from flask import Flask
import random
import os
from scaler import scale_decision

app = Flask(__name__)

@app.route('/')
def home():
    current_load = random.randint(10, 100)
    servers, predicted_load = scale_decision()

    return f"""
    <h1>Cloud Auto-Scaler Dashboard</h1>
    <p>Current Load: {current_load}%</p>
    <p>Predicted Load: {predicted_load:.2f}%</p>
    <p>Active Servers: {servers}</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
   
