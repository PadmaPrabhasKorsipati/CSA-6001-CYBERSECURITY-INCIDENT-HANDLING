import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score

print("===== FALSE POSITIVE & TRUE INCIDENT ANALYSIS =====\n")

# Step 1: Load dataset
data = pd.read_csv("alerts.csv")

print("Dataset Loaded Successfully\n")
print(data)
print("\n-----------------------------------\n")

# Step 2: Convert labels to numeric
# Attack = 1, Normal = 0
data['predicted'] = data['predicted_label'].map({'Attack':1, 'Normal':0})
data['actual'] = data['actual_label'].map({'Attack':1, 'Normal':0})

# Step 3: Generate Confusion Matrix
tn, fp, fn, tp = confusion_matrix(data['actual'], data['predicted']).ravel()

print("Confusion Matrix Values:")
print(f"True Positive (TP): {tp}")
print(f"False Positive (FP): {fp}")
print(f"False Negative (FN): {fn}")
print(f"True Negative (TN): {tn}")
print("\n-----------------------------------\n")

# Step 4: Calculate Metrics
precision = precision_score(data['actual'], data['predicted'])
recall = recall_score(data['actual'], data['predicted'])
accuracy = accuracy_score(data['actual'], data['predicted'])

print("Performance Metrics:")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"Accuracy: {accuracy:.2f}")

print("\nAnalysis Completed Successfully.")
