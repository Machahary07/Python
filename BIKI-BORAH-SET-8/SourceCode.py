from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load the dataset using Pandas and display its contents.
import pandas as pd
df = pd.read_excel(r'D:\PYTHON\SET-8\SET-8.xlsx')
print(df)

# 2. Handle any missing values present in the dataset appropriately.
df = df.dropna()
print(df)

# 3. Display independent features (X).
X = df[['ground_clearance', 'height']]
print(X)

# Target variable (y)
y = df['category']

# 4. Perform classification using a 70%-30% train-test split.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 5. Display the accuracy of the model.
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of the model:", accuracy)