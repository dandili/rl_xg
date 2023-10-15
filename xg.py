import json
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the JSON file
file_path = 'your_file_path_here.json'  # Replace with your JSON file path
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract ball positions and shot events
network_frames = data.get('network_frames', [])
ball_positions = []
shot_events = []

for frame in network_frames:
    for actor in frame['updated_actors']:
        if 'RigidBody' in actor.get('attribute', {}):
            position = actor['attribute']['RigidBody']['location']
            time = frame['time']
            ball_positions.append((time, position))

# Define assumptions and identify shot events
min_y = -51.75
max_y = 52.18
shot_threshold = 40

for position in ball_positions:
    time, coordinates = position
    y_coordinate = coordinates['y']
    
    if abs(y_coordinate) > shot_threshold:
        shot_events.append((time, coordinates))

# Simulate goal outcomes
shots_data = []

for event in shot_events:
    time, coordinates = event
    goal_y = max_y if coordinates['y'] > 0 else min_y
    distance_to_goal = math.sqrt((coordinates['x'] - 0)**2 + (coordinates['y'] - goal_y)**2 + (coordinates['z'] - 0)**2)
    goal_outcome = 1 if distance_to_goal < 10 else 0
    shots_data.append((time, coordinates, distance_to_goal, goal_outcome))

# Prepare data for the xG model
X = [[item[2]] for item in shots_data]  # Feature: distance to the goal
y = [item[3] for item in shots_data]    # Target variable: simulated goal outcome

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model's accuracy
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the model to a file
from joblib import dump
dump(model, 'xG_model.joblib')
