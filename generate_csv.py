import pandas as pd
import random

print("Generating synthetic IDS dataset...")

# Define our labels
labels = ['Normal', 'Attack']

# 1. Generate 1000 actual network events (85% Normal, 15% Attack)
actual_labels = random.choices(labels, weights=[85, 15], k=1000)

# 2. Simulate the Intrusion Detection System's predictions
predicted_labels = []
for actual in actual_labels:
    if actual == 'Attack':
        # The system correctly catches 80% of attacks (True Positives)
        # but misses 20% of them (False Negatives)
        prediction = random.choices(['Attack', 'Normal'], weights=[80, 20], k=1)[0]
    else:
        # The system correctly ignores 95% of normal traffic (True Negatives)
        # but falsely alerts on 5% of it (False Positives)
        prediction = random.choices(['Normal', 'Attack'], weights=[95, 5], k=1)[0]
        
    predicted_labels.append(prediction)

# 3. Build the DataFrame
df = pd.DataFrame({
    'predicted_label': predicted_labels,
    'actual_label': actual_labels
})

# 4. Export to CSV in the current directory
df.to_csv('alerts.csv', index=False)

print("Success! 'alerts.csv' has been created with 1,000 rows.")