import pandas as pd
import numpy as np

data = {
    'Student ID': range(1, 101),
    'Age': np.random.randint(18, 25, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Subject 1': np.random.randint(50, 100, 100),
    'Subject 2': np.random.randint(60, 90, 100),
    'Subject 3': np.random.randint(55, 95, 100),
    'Attendance': np.random.uniform(70, 100, 100),
    'Final Grade': np.random.choice(['A', 'B', 'C'], 100)
}

df = pd.DataFrame(data)

df.loc[5, 'Subject 1'] = np.nan
df.loc[20, 'Subject 2'] = np.nan
df.loc[35, 'Attendance'] = np.nan

missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

df['Subject 1'].fillna(df['Subject 1'].mean(), inplace=True)
df['Subject 2'].fillna(df['Subject 2'].median(), inplace=True)
df['Attendance'].fillna(df['Attendance'].mean(), inplace=True)

df['Attendance'] = df['Attendance'].clip(0, 100)

df['Final Grade'] = df['Final Grade'].apply(
    lambda x: x if x in ['A', 'B', 'C'] else 'C'
)

missing_values_after = df.isnull().sum()

print("\nMissing Values After Imputation:\n", missing_values_after)


import numpy as np

def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

outliers_subject_1 = detect_outliers(df, 'Subject 1')
print("\nOutliers in Subject 1:\n", outliers_subject_1)

Q1 = df['Subject 1'].quantile(0.25)
Q3 = df['Subject 1'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df['Subject 1'] = np.clip(df['Subject 1'], lower_bound, upper_bound)

outliers_subject_2 = detect_outliers(df, 'Subject 2')
print("\nOutliers in Subject 2:\n", outliers_subject_2)

print("Skewness of Subject 1 before transformation:", df['Subject 1'].skew())

df['Subject 1'] = np.log(df['Subject 1'] + 1)

print("Skewness of Subject 1 after transformation:", df['Subject 1'].skew())