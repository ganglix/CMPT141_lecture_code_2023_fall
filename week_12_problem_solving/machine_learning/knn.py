from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

# Example data: features could represent different measurements or characteristics
# Here, we're using random data for illustration purposes
np.random.seed(0)
cats = np.random.rand(50, 2)  # 50 cats with 2 features
dogs = np.random.rand(50, 2) + 0.5  # 50 dogs with 2 features

# Labels: 0 for cats, 1 for dogs
labels = np.array([0]*50 + [1]*50)

print(cats)

# # Combine the data
# data = np.vstack([cats, dogs])
#
# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=0)
#
# # Create KNN classifier
# knn = KNeighborsClassifier(n_neighbors=3)
#
# # Fit the classifier to the data
# knn.fit(X_train, y_train)
#
# # Make predictions on the test data
# predictions = knn.predict(X_test)
#
# # Calculate accuracy and classification report
# accuracy = accuracy_score(y_test, predictions)
# report = classification_report(y_test, predictions)
#
# print(f"Accuracy: {accuracy}")
# print("Classification Report:")
# print(report)
