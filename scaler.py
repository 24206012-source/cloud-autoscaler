from model import predict_load

# Simulated cloud instances
servers = 1

def scale_up():
    global servers
    servers += 1
    print(f"⚡ Scaling UP → Servers: {servers}")

def scale_down():
    global servers
    if servers > 1:
        servers -= 1
    print(f"🔻 Scaling DOWN → Servers: {servers}")

def scale_decision():
    global servers

    print("Running Auto-Scaler...")

    prediction = predict_load(11)
    print(f"Predicted Load: {prediction}")

    if prediction > 75:
        scale_up()
    elif prediction < 30:
        scale_down()
    else:
        print("✅ No scaling needed")

    return servers, prediction
