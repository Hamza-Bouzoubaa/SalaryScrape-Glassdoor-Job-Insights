import pandas as pd 
df = pd.read_excel("output2.xlsx")

#Salary
df = df[df["Salary"]!=-1]
Salary = df["Salary"].apply(lambda x: x.split('(')[0])
df['hourly'] = df['Salary'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Employer provided'] = df['Salary'].apply(lambda x: 1 if '(Employer est.)' in x else 0)
Salary = Salary.apply(lambda x: x.replace('K','').replace('$',''))
Salary = Salary.apply(lambda x: x.replace('Per Hour',''))
df['Min_Salary'] = Salary.apply(lambda x: float(x.split('-')[0]))
df['Max_Salary'] = Salary.apply(lambda x: float(x.split('-')[-1]))
df['Average Salary'] = (df.Min_Salary + df.Max_Salary)/2
  
#Location 
df['Job_State'] = df['Location'].apply(lambda x: x.split(',')[1])
df['Job_City'] = df['Location'].apply(lambda x: x.split(',')[0])
x= df.Job_State.value_counts()


#age 
df['age'] = df.Founded.apply(lambda x: str(x).split()[0])
df['age'] = df.age.apply(lambda x: x if (x[0]==str(1) or x[0]==str(2) ) else 0 )
df['age'] = df.age.apply(lambda x:( 2023 - int(x)))

#Job description 
df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['r_Studio'] = df['Job Description'].apply(lambda x: 1 if ('r studio' in x.lower() or 'r-studio' in x.lower()) else 0)
df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

print(df.excel.value_counts())


print(df.columns)
df = df.drop('Unnamed: 0',axis=1)
df.to_csv("Clean data.csv")