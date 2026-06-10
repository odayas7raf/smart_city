from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pickle

# Generate training data
np.random.seed(42)
n_samples = 1000

vehicle_count = np.random.randint(10, 200, n_samples)
time_of_day = np.random.randint(0, 24, n_samples)
day_of_week = np.random.randint(0, 7, n_samples)

# Label: 0=low, 1=medium, 2=high
labels = []
for v, t, d in zip(vehicle_count, time_of_day, day_of_week):
    if v < 60:
        labels.append(0)
    elif v < 130:
        labels.append(1)
    else:
        labels.append(2)

X = np.column_stack([vehicle_count, time_of_day, day_of_week])
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
with open('traffic_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as traffic_model.pkl")

# Test prediction
test = np.array([[150, 8, 1]])
prediction = model.predict(test)
labels_map = {0: 'low', 1: 'medium', 2: 'high'}
print(f"Test prediction (150 vehicles, 8am, Monday): {labels_map[prediction[0]]}")