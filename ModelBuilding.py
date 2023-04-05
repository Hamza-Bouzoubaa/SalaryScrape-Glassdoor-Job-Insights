import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


df = pd.read_csv('eda_data.csv')

print(df.columns)

df_model = df[['Average Salary','Rating','Size','Industry','Revenue','hourly','Employer provided','Job_State','age','Python','aws','Spark','excel','seniority','job_simplified','desc_len']]

# get dummy data 
df_dum = pd.get_dummies(df_model)
df_dum.to_csv('dummies.csv')

# train test split 

X = df_dum.drop('Average Salary', axis=1)
y = df_dum['Average Salary'].values


X_train, X_test, y_train,y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

print(X.columns)

model = LinearRegression()
model.fit(X_train,y_train)
print(model.score(X_test,y_test))

np.mean(cross_val_score(model,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))


def Salary(model,Rating, hourly, Employerprovided, age, Python, aws,Spark, excel):
    x = np.array([Rating, hourly, Employerprovided, age, Python, aws,Spark, excel]).reshape(1,8)
    return model.predict(x)


C = Salary(model,4,1,1,50,1,1,1,1)
print()

