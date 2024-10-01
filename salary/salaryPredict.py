import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import sys

data = pd.read_csv("salary_data.csv")
x = data["YearsExperience"]
x=x.values
x=x.reshape(30,1)
y = data["Salary"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x, y, test_size=0.20, random_state=42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model=model.fit(X_test,y_test)

a=sys.argv

pre= model.predict([[a[1]]])

print("predicted Salary :",pre)
