import qrcode
from sklearn.tree import DecisionTreeClassifier

# Training data for a simple classification problem
X_train = [[0], [1], [2], [3]]
y_train = ['A', 'B', 'C', 'D']

# Train a decision tree classifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Example data point for prediction
data_point = [[2.5]]  # New data point

# Predict the class label using the trained classifier
predicted_label = classifier.predict(data_point)[0]

# Generate QR code with the predicted class label
qr = qrcode.make(predicted_label)

# Save the QR code image
qr.save("predicted_label_qr_code.png")

print(f"QR code generated successfully with the predicted label: {predicted_label}")
