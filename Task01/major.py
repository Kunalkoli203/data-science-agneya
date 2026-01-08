import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#all the required data 
data = {
    "Marks": [35, 45, 60, 70, 80, 90, 30, 55],
    "Attendance": [60, 65, 75, 80, 85, 90, 50, 70],
    "Result": [0, 0, 1, 1, 1, 1, 0, 1]   # 0 = Fail, 1 = Pass
}

df = pd.DataFrame(data)
X = df[["Marks", "Attendance"]]
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1
)
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

new_student = [[65, 75]]   
result = model.predict(new_student)

if result[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")
