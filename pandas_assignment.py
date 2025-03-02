import pandas as pd

#1
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}

df = pd.DataFrame(data)

#1A
print(df.head())

#1B
summary_stats = df[['Age', 'Salary']].describe()
print(summary_stats)

#1C
avg_salary_hr = df[df['Department'] == 'HR']['Salary'].mean()
print(f"Average salary in HR department: {avg_salary_hr}")

#2
df['Bonus'] = df['Salary'] * 0.10
print(df)

#3
filtered_df = df[(df['Age'] >= 25) & (df['Age'] <= 30)]
print(filtered_df)

#4
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print(avg_salary_by_dept)

#5
df_sorted = df.sort_values(by='Salary', ascending=True)
df_sorted.to_csv('sorted_salaries.csv', index=False)
print("Sorted DataFrame saved to 'sorted_salaries.csv'")
