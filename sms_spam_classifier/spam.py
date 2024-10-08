import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv('SMSSpamCollection.csv', sep='\t', names=['label', 'message'])

# Data Preprocessing
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Text Vectorization
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train Model
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

# Make Predictions
predictions = classifier.predict(X_test_vectorized)

# Evaluate Model
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)
print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{report}')

# Take User Input
user_input = input('Enter SMS Message: ')
user_input_vectorized = vectorizer.transform([user_input])
prediction = classifier.predict(user_input_vectorized)

if prediction[0] == 1:
    print(' Hey! It is a Spam SMS..!')
else:
    print('Dont worry! It is a Non-Spam SMS..!')