import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("churn.csv")

# Basic info
print("First 5 rows:\n", df.head())
print("\nData Info:\n")
print(df.info())

# Convert TotalCharges to numeric FIRST
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Now remove missing values
df = df.dropna()

# Convert target
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Drop ID
df = df.drop('customerID', axis=1)

# Encode categorical variables
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

for col in df.select_dtypes(include=['object', 'string']).columns:
    df[col] = le.fit_transform(df[col])

# Split features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Scale the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split using scaled data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Train model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("\nModel Accuracy:", accuracy)

# Feature importance
importance = pd.Series(model.coef_[0], index=df.drop('Churn', axis=1).columns)
print("\nTop Features:\n", importance.sort_values(ascending=False).head(10))

# Save cleaned data for Power BI
df.to_csv("cleaned_churn.csv", index=False)

print("\nCleaned data saved as cleaned_churn.csv")
