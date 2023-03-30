import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('Clean data.csv')
df.head()


def title_simplifier(title):
    if 'data scientist' in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst' in title.lower():
        return 'analyst'
    elif 'machine learning' in title.lower():
        return 'mle'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'director' in title.lower():
        return 'director'
    else:
        return 'na'
    

    
def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'
    
df['job_simp'] = df['JobTitle'].apply(title_simplifier)
print(df.job_simp.value_counts())


df['seniority'] = df['JobTitle'].apply(seniority)
print(df.seniority.value_counts())


print(df.Job_State.value_counts())


#hourly wage to annual 

df['Min_Salary'] = df.apply(lambda x: x.Min_Salary*2 if x.hourly ==1 else x.Min_Salary, axis =1)
df['Max_Salary'] = df.apply(lambda x: x.Max_Salary*2 if x.hourly ==1 else x.Max_Salary, axis =1)


df['Company'] = df.Company.apply(lambda x: x.replace('\n', ''))


df.describe()

df.to_csv("Clean data.csv")