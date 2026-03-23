from flask import Flask
import random
from scaler import scale_decision
import os

app = Flask(__name__)

@app.route('/')
def home():
    current_load = random.randint(10, 100)
    servers, predicted_load = scale_decision()

    return f"""
    <html>
    <head>
    <meta http-equiv="refresh" content="5">
    <title>Cloud Auto-Scaler</title>

    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
    body {{
        margin: 0;
        font-family: Arial;
        background: #0f172a;
        color: white;
        text-align: center;
    }}

    .navbar {{
        background: #020617;
        padding: 15px;
        font-size: 22px;
    }}

    .container {{
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
    }}

    .card {{
        background: #1e293b;
        padding: 20px;
        border-radius: 15px;
        width: 220px;
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
        transition: 0.3s;
        border: 1px solid rgba(255,255,255,0.1);
    }}

    .card:hover {{
        transform: scale(1.08);
        box-shadow: 0 0 25px rgba(34,197,94,0.5);
    }}

    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
        100% {{ transform: scale(1); }}
    }}

    .value {{
        font-size: 28px;
        margin-top: 10px;
        animation: pulse 2s infinite;
    }}

    .green {{ color: #22c55e; }}
    .yellow {{ color: #facc15; }}
    .red {{ color: #ef4444; }}

    canvas {{
        margin-top: 40px;
    }}

    ul {{
        list-style: none;
        padding: 0;
    }}

    li {{
        padding: 8px;
        background: #334155;
        margin: 5px;
        border-radius: 8px;
    }}

    </style>
    </head>

    <body>

    <div class="navbar">☁️ Cloud Monitoring Panel</div>

    <h1>AI-Based Smart Auto-Scaler</h1>

    <div class="container">

        <div class="card">
            <h3>Current Load</h3>
            <div class="value {'red' if current_load>75 else 'yellow' if current_load>40 else 'green'}">
                {current_load}%
            </div>
        </div>

        <div class="card">
            <h3>Predicted Load</h3>
            <div class="value {'red' if predicted_load>75 else 'yellow' if predicted_load>40 else 'green'}">
                {predicted_load:.2f}%
            </div>
        </div>

        <div class="card">
            <h3>Active Servers</h3>
            <div class="value">
                {servers}
            </div>
        </div>

    </div>

    <h2>
        {'🚨 HIGH LOAD - Scaling Up' if predicted_load>75 else 
         '⚠️ MEDIUM LOAD' if predicted_load>40 else 
         '✅ NORMAL LOAD'}
    </h2>

    <!-- GRAPH -->
    <canvas id="myChart" width="600" height="250"></canvas>

    <script>
    const ctx = document.getElementById('myChart');

    new Chart(ctx, {{
        type: 'line',
        data: {{
            labels: ['Current', 'Predicted'],
            datasets: [{{
                label: 'Load %',
                data: [{current_load}, {predicted_load}],
                borderWidth: 3,
                tension: 0.4
            }}]
        }},
        options: {{
            scales: {{
                y: {{
                    beginAtZero: true,
                    max: 120
                }}
            }}
        }}
    }});
    </script>

    <!-- SERVER LIST -->
    <h2>Server Instances</h2>
    <ul>
        {''.join([f"<li>Server {i+1} - Running</li>" for i in range(servers)])}
    </ul>

    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
