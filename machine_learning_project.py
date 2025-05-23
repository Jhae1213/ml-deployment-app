# -*- coding: utf-8 -*-
"""Machine Learning Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/164RdOJ9EOE0eh6_WPqBAcSYY5TF-KUUe
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, LabelEncoder

# load file
from google.colab import drive
drive.mount('/content/MyDrive')

drive_path = '/content/MyDrive/MyDrive/IT_IM82/Diabetes.csv'

df = pd.read_csv(drive_path)

df.head()

# Drop fully empty columns and rename unnamed columns appropriately
df = df.dropna(axis=1, how='all')

# Clean column names by removing extra quotes and whitespace
df.columns = df.columns.str.replace("'", "").str.strip()

# Select relevant features and target variable
features = ['preg', 'plas', 'pres', 'skin', 'insu', 'mass', 'pedi', 'age']
target = 'class'

# Exploratory Data Analysis
eda_results = {}

# Class balance
class_counts = y.value_counts()
eda_results["class_balance"] = class_counts

# Missing values
missing_data = df[features + [target]].isnull().sum()
eda_results["missing_data"] = missing_data

# Split the data into features and target variable
X = df[features]
y = df[target]

# Step 4: Visualization
plt.figure(figsize=(6,4))
sns.countplot(x=target, data=df)
plt.xlabel("Class")
plt.ylabel("Count")
plt.title("Class Balance")
plt.tight_layout()
plt.show()

#Split the dataset

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

eda_results["train_shape"] = X_train.shape
eda_results["test_shape"] = X_test.shape

eda_results

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize feature values
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""Logistic Regression"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay

# Features and target
features = ['preg', 'plas', 'pres', 'skin', 'insu', 'mass', 'pedi', 'age']
target = 'class'

X = df[features]
y = df[target]

# Convert target labels to numerical using LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Logistic Regression model
logreg = LogisticRegression(max_iter=200)
logreg.fit(X_train, y_train)

# Logistic Regression
lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

# Metrics
acc = accuracy_score(y_test, y_pred_lr)
prec = precision_score(y_test, y_pred_lr)
rec = recall_score(y_test, y_pred_lr)
f1 = f1_score(y_test, y_pred_lr)

print("Logistic Regression Performance:")
print("Accuracy :", round(acc, 4))
print("Precision:", round(prec, 4))
print("Recall   :", round(rec, 4))
print("F1 Score :", round(f1, 4))

# Predict using the test set
logreg_preds = logreg.predict(X_test)

# Evaluate the model
report = classification_report(y_test, logreg_preds)
print("Classification Report:")
print(report)

# Plot Confusion Matrix
cm = confusion_matrix(y_test, logreg_preds)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.title('Logistic Regression Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

"""Decision Tree"""

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

acc_dt = accuracy_score(y_test, y_pred_dt)
prec_dt = precision_score(y_test, y_pred_dt)
rec_dt = recall_score(y_test, y_pred_dt)
f1_dt = f1_score(y_test, y_pred_dt)

print("Accuracy :", round(acc_dt, 4))
print("Precision:", round(prec_dt, 4))
print("Recall   :", round(rec_dt, 4))
print("F1 Score :", round(f1_dt, 4))


ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred_dt)).plot()
plt.title("Confusion Matrix - Decision Tree")
plt.show()

# Evaluate the model
print("Decision Tree Classifier Performance:")
print(classification_report(y_test, y_pred_dt))

"""Random Forest"""

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# Metrics
acc_rf = accuracy_score(y_test, y_pred_rf)
prec_rf = precision_score(y_test, y_pred_rf)
rec_rf = recall_score(y_test, y_pred_rf)
f1_rf = f1_score(y_test, y_pred_rf)

print("Accuracy :", round(acc_rf, 4))
print("Precision:", round(prec_rf, 4))
print("Recall   :", round(rec_rf, 4))
print("F1 Score :", round(f1_rf, 4))

ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred_rf)).plot()
plt.title("Confusion Matrix - Random Forest")
plt.show()

# Evaluate the model
print("Random Forest Classifier Performance:")
print(classification_report(y_test, y_pred_rf))

"""Naive Bayes"""

from sklearn.naive_bayes import GaussianNB

# Train Naive Bayes model
nb = GaussianNB()
nb.fit(X_train, y_train)

# Predict using the test set for Naive Bayes
y_pred_nb = nb.predict(X_test)

# Metrics
acc_nb = accuracy_score(y_test, y_pred_nb)
prec_nb = precision_score(y_test, y_pred_nb)
rec_nb = recall_score(y_test, y_pred_nb)
f1_nb = f1_score(y_test, y_pred_nb)

print("Accuracy :", round(acc_nb, 4))
print("Precision:", round(prec_nb, 4))
print("Recall   :", round(rec_nb, 4))
print("F1 Score :", round(f1_nb, 4))
# Confusion Matrix
cm_nb = confusion_matrix(y_test, y_pred_nb)
ConfusionMatrixDisplay(confusion_matrix=cm_nb).plot(cmap='Greys')
plt.title("Confusion Matrix - Naive Bayes")
plt.show()

# Evaluate the model
print("Naive Bayes Classifier Performance:")
print(classification_report(y_test, y_pred_nb))

"""KNN"""

# Import necessary libraries
from sklearn.neighbors import KNeighborsClassifier
# KNN Classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
# Train a KNN classifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)
# Metrics
acc_knn = accuracy_score(y_test, y_pred_knn)
prec_knn = precision_score(y_test, y_pred_knn)
rec_knn = recall_score(y_test, y_pred_knn)
f1_knn = f1_score(y_test, y_pred_knn)

print("K-Nearest Neighbors (KNN) Performance:")
print("Accuracy :", round(acc_knn, 4))
print("Precision:", round(prec_knn, 4))
print("Recall   :", round(rec_knn, 4))
print("F1 Score :", round(f1_knn, 4))
# Calculate confusion matrix
# Use y_pred_knn instead of y_pred
conf_matrix = confusion_matrix(y_test, y_pred_knn)
# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='d', xticklabels=classifier.classes_, yticklabels=classifier.classes_)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# Evaluate the classifier
report = classification_report(y_test, y_pred_knn)
print("Classification Report:")
print(report)

"""SVM"""

from sklearn.svm import SVC

# Train SVM model
svm = SVC(kernel='linear', probability=True)
svm.fit(X_train, y_train)

# Predict
y_pred_svm = svm.predict(X_test)

# Metrics
acc_svm = accuracy_score(y_test, y_pred_svm)
prec_svm = precision_score(y_test, y_pred_svm)
rec_svm = recall_score(y_test, y_pred_svm)
f1_svm = f1_score(y_test, y_pred_svm)

print("Accuracy :", round(acc_svm, 4))
print("Precision:", round(prec_svm, 4))
print("Recall   :", round(rec_svm, 4))
print("F1 Score :", round(f1_svm, 4))

# Confusion Matrix
cm_svm = confusion_matrix(y_test, y_pred_svm)
ConfusionMatrixDisplay(confusion_matrix=cm_svm).plot(cmap='Reds')
plt.title("Confusion Matrix - SVM")
plt.show()

# Evaluate the model
print("Support Vector Machine (SVM) Performance:")
print(classification_report(y_test, y_pred_svm))

pip install mlflow

pip install pyngrok

import os
os.makedirs('artifacts', exist_ok=True)

from pyngrok import ngrok
import subprocess
import time
import os # Import os if not already imported

# Add your ngrok authtoken BEFORE connecting
# Replace "YOUR_AUTHTOKEN" with your actual authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
ngrok.set_auth_token("2xRUQ5xEwywlWYVp5SkFrHooonv_5Kx9CSMbrjQpg8KvLAjWf")

ngrok.kill()  # Stop previous tunnels if any

# Start MLflow UI on port 5000
# Check if the process is already running to avoid multiple instances
try:
    mlflow_ui = subprocess.Popen(["mlflow", "ui", "--port", "5000"], preexec_fn=os.setsid)
    print("MLflow UI process started.")
    time.sleep(5)  # Let MLflow load
except Exception as e:
    print(f"Could not start MLflow UI process: {e}")


# Open ngrok tunnel
try:
    mlflow_tunnel = ngrok.connect(5000)
    print("✅ Open MLflow UI here:", mlflow_tunnel.public_url)
except Exception as e:
    print(f"Error connecting ngrok: {e}")
    print("Please ensure your ngrok authtoken is correct and ngrok is installed.")
    # You might want to check ngrok status here as well
    # result = subprocess.run(["ngrok", "version"], capture_output=True, text=True)
    # print("ngrok version check:", result.stdout)

from pyngrok import ngrok
import subprocess
import time
import os # Import os if not already imported
import mlflow # Import mlflow if not already imported

ngrok.kill()  # Stop previous tunnels if any

# Define a log directory for the MLflow tracking server
log_dir = "mlruns"
os.makedirs(log_dir, exist_ok=True)

# Start MLflow tracking server on port 5000 using file storage
# Use `!` to run as a shell command in Colab, ensuring it runs in the background
# We direct output to /dev/null to keep the cell clean
# Check if MLflow server is already running before starting another one
try:
    subprocess.run(["pgrep", "-f", "mlflow server"], check=True, stdout=subprocess.PIPE).stdout.decode().strip()
    print("MLflow server is already running.")
except subprocess.CalledProcessError:
    print("Starting MLflow server...")
    !mlflow server --backend-store-uri file://{log_dir} --port 5000 > /dev/null 2>&1 &
    time.sleep(10)  # Give the server more time to start
    print("MLflow server started.")


# Open ngrok tunnel
try:
    mlflow_tunnel = ngrok.connect(5000)
    print("✅ Open MLflow UI here:", mlflow_tunnel.public_url)

    # Now, set the tracking URI to the ngrok public URL
    mlflow.set_tracking_uri(mlflow_tunnel.public_url)
    print("MLflow tracking URI set.")

except Exception as e:
    print(f"Error starting ngrok tunnel: {e}")
    print("Please check if the MLflow server is running and the ngrok authtoken is configured correctly.")

# Ensure necessary libraries are imported
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from IPython import get_ipython
from IPython.display import display

# load file
from google.colab import drive
drive.mount('/content/MyDrive')

drive_path = '/content/MyDrive/MyDrive/IT_IM82/Diabetes.csv'

df = pd.read_csv(drive_path)

# Drop fully empty columns and rename unnamed columns appropriately
df = df.dropna(axis=1, how='all')
# Clean column names by removing extra quotes and whitespace
df.columns = df.columns.str.replace("'", "").str.strip()

# Select relevant features and target variable
features = ['preg', 'plas', 'pres', 'skin', 'insu', 'mass', 'pedi', 'age']
target = 'class'

# Exploratory Data Analysis
eda_results = {}

# Class balance
class_counts = y.value_counts()
eda_results["class_balance"] = class_counts

# Missing values
missing_data = df[features + [target]].isnull().sum()
eda_results["missing_data"] = missing_data

# Split the data into features and target variable
X = df[features]
y = df[target]

#Split the dataset

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

eda_results["train_shape"] = X_train.shape
eda_results["test_shape"] = X_test.shape

eda_results

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize feature values
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Set or create the experiment BEFORE starting runs
experiment_name = "ML_Project_Experiment"
try:
    # Attempt to get the experiment by name
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        # If experiment does not exist, create it
        experiment_id = mlflow.create_experiment(experiment_name)
        print(f"Created experiment: {experiment_name} with ID: {experiment_id}")
    else:
        # If experiment exists, get its ID
        experiment_id = experiment.experiment_id
        print(f"Using existing experiment: {experiment_name} with ID: {experiment_id}")

    # ✅ Set the experiment ID explicitly so the upcoming runs attach to it
    mlflow.set_experiment(experiment_name)

except Exception as e:
    print(f"Error setting or creating MLflow experiment: {e}")

# Enable auto-logging for scikit-learn only once
mlflow.sklearn.autolog()

"""Random Forest"""

#Random Forest

# Start an MLflow run using the correct experiment ID
with mlflow.start_run(run_name="Random Forest Autologged", experiment_id=experiment_id):
    model = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    print(f"✅ Random Forest model trained and logged with accuracy: {acc}")

"""Logistic"""

#logistic

from sklearn.linear_model import LogisticRegression

# Enable autologging again (optional if already enabled)
mlflow.sklearn.autolog()

# Start new run
with mlflow.start_run():
    logreg_model = LogisticRegression(max_iter=200)
    logreg_model.fit(X_train, y_train)
    preds = logreg_model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"✅ Logistic Regression accuracy: {acc}")

"""Decision Tree"""

#Decision Tree

from sklearn.tree import DecisionTreeClassifier

# Enable autologging again (optional if already enabled earlier in the notebook)
mlflow.sklearn.autolog()

# Start new MLflow run
with mlflow.start_run(run_name="Decision Tree Autologged"):
    dt_model = DecisionTreeClassifier(max_depth=3, random_state=42)  # You can tune max_depth as needed
    dt_model.fit(X_train, y_train)
    preds = dt_model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"✅ Decision Tree accuracy: {acc}")

"""Naive Bayes"""

#Naive Bayes

from sklearn.naive_bayes import GaussianNB

mlflow.sklearn.autolog()

with mlflow.start_run(run_name="Naive Bayes Autologged"):
    nb_model = GaussianNB()
    nb_model.fit(X_train, y_train)
    preds = nb_model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"✅ Naive Bayes accuracy: {acc}")

"""KNN"""

#KNN

from sklearn.neighbors import KNeighborsClassifier

mlflow.sklearn.autolog()

with mlflow.start_run(run_name="KNN Autologged"):
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    preds = knn_model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"✅ KNN accuracy: {acc}")

"""SVm"""

#SVM

from sklearn.svm import SVC

mlflow.sklearn.autolog()

with mlflow.start_run(run_name="SVM Autologged"):
    svm_model = SVC(C=1.0, kernel='rbf', probability=True, random_state=42)
    svm_model.fit(X_train, y_train)
    preds = svm_model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"✅ SVM accuracy: {acc}")

import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://localhost:5000")  # Or leave empty for local
mlflow.set_experiment("ML_Project_Experiment")

best_model_name = "Random Forest"
print(f"Best Model : {best_model_name}")

import joblib

# Save the trained Random Forest model using the correct variable name and filename
joblib.dump(model, "best_model_randomforest.pkl")

print("✅ Best model saved as 'best_model_randomforest.pkl'")

# Final prediction using best model (SVM)
final_predictions = model.predict(X_test)

# Display confusion matrix
ConfusionMatrixDisplay(confusion_matrix(y_test, final_predictions)).plot()
plt.title("Confusion Matrix - Best Model (Random Forest)")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Model accuracy data
accuracy_data = {
    "Model": [
        "Random Forest",
        "Logistic Regression",
        "Decision Tree",
        "Naive Bayes",
        "KNN",
        "SVM"
    ],
    "Accuracy": [
        0.7727,
        0.7532,
        0.7597,
        0.7662,
        0.6948,
        0.7338
    ]
}

# Create DataFrame
df_accuracy = pd.DataFrame(accuracy_data)

# Sort by accuracy descending
df_sorted = df_accuracy.sort_values(by="Accuracy", ascending=False).reset_index(drop=True)

# Display table
print(df_sorted)

# Optional: Plotting bar chart
plt.figure(figsize=(10, 6))
plt.barh(df_sorted["Model"], df_sorted["Accuracy"], color="skyblue")
plt.xlabel("Accuracy")
plt.title("Model Accuracy Comparison")
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

pip install streamlit

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('best_model_randomforest.pkl')

st.title("ML Model Prediction App")

# Option for user to upload CSV or input manually
upload_option = st.radio("Choose input method:", ("Manual Input", "Upload CSV"))

if upload_option == "Manual Input":
    # Create input fields (example with 4 features)
    feature1 = st.number_input("Feature 1", step=0.01)
    feature2 = st.number_input("Feature 2", step=0.01)
    feature3 = st.number_input("Feature 3", step=0.01)
    feature4 = st.number_input("Feature 4", step=0.01)

    input_data = pd.DataFrame([[feature1, feature2, feature3, feature4]],
                              columns=["feature1", "feature2", "feature3", "feature4"])

    if st.button("Predict"):
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Class: {prediction}")

elif upload_option == "Upload CSV":
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        predictions = model.predict(data)
        st.write("Predictions:")
        st.write(predictions)

# Display performance summary (replace with your real values)
st.markdown("### 📊 Model Performance")
st.write("**Accuracy:** 77.27%")
st.write("**Confusion Matrix:**")
# Optional: add real confusion matrix image or table



