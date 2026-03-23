import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv('data.csv')

X = data[['time']]
y = data['load']

# Train model
model = LinearRegression()
model.fit(X, y)

def predict_load(next_time):
    return model.predict([[next_time]])[0]

# Test
if __name__ == "__main__":
    print("Testing model...")
    print("Predicted Load:", predict_load(11))
