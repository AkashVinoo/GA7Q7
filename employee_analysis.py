import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample employee data
data = {
    'EmployeeID': range(1, 101),
    'Department': ['R&D']*35 + ['Sales']*30 + ['HR']*15 + ['Marketing']*10 + ['Finance']*10,
    'Region': ['North', 'South', 'East', 'West'] * 25
}
df = pd.DataFrame(data)

# Calculate and print R&D department frequency
rd_count = df['Department'].value_counts()['R&D']
print("R&D Department Count:", rd_count)

# Plot histogram
plt.figure(figsize=(8, 6))
sns.countplot(x='Department', data=df, palette='Set2')
plt.title('Employee Count by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("department_distribution.png")
