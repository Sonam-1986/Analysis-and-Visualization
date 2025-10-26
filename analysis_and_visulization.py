# -*- coding: utf-8 -*-

from google.colab import files


uploaded = files.upload()


for filename in uploaded.keys():
    print(f'Uploaded file: {filename}')

import pandas as pd

# Load the CSV file
df = pd.read_csv('employee.csv')

# Display the first few rows
print(df.head())

average_salary = df['Salary'].mean()
print("Average Salary:", average_salary)

avg_salary_dept = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(avg_salary_dept)

# Bar chart: Average salary by department
plt.figure(figsize=(8,5))
avg_salary_dept.plot(kind='bar', color='teal')
plt.title('Average Salary by Department')
plt.ylabel('Average Salary')
plt.xlabel('Department')
plt.tight_layout()
plt.show()

# Scatter plot: Salary vs. Experience
plt.figure(figsize=(8,5))
plt.scatter(df['Experience'], df['Salary'], c='orchid')
plt.title('Salary vs. Experience')
plt.xlabel('Experience (years)')
plt.ylabel('Salary')
plt.tight_layout()
plt.show()

# Heatmap: Correlation between numeric columns
plt.figure(figsize=(6,4))
sns.heatmap(df[['Age', 'Salary', 'Experience']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Insights:
print("\nInsights and Observations:")
print("- The average salary across all employees is {:.2f}.".format(average_salary))
print("- There are significant salary outliers (e.g., very high salaries in Finance).")
print("- Departments like IT and CS have higher average salaries compared to HR and Analyst.")
print("- There is a positive trend between Experience and Salary, but with some outlier salaries.")
print("- The heatmap shows the correlation between Age, Salary, and Experience. Salary is moderately correlated with Experience, but outliers may influence this.")