from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load the dataset using Pandas and display its contents.
import pandas as pd
df = pd.read_excel(r'D:\PYTHON\BIKI-BORAH-SET-9\SET-9.xlsx')
print(df)

# Remove missing values if any
df = df.dropna()

# Independent features (X) and target (y)
X = df[['ground_clearance', 'height']]  # change columns if needed
y = df['category']

# 2. Perform classification using a 70%-30% train-test split.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 3. Display training data (X_train).
print("Training data (X_train):")
print(X_train)

# 4. Apply logistic regression for classification.
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Display the accuracy for the model.
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of the model:", accuracy)
