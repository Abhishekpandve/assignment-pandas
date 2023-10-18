#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
df = pd.read_csv(url)

# Task 1: Identify the dimensions of the dataset
num_rows, num_columns = df.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

# Task 2: Determine data types and make corrections if needed

print(df.dtypes)



# Task 3: Identify the number of unique values and categorical columns
unique_counts = df.nunique()
categorical_columns = [col for col in df.columns if unique_counts[col] < num_rows]

# Describe unique values of categorical columns
for col in categorical_columns:
    unique_values = df[col].unique()
    print(f"Column '{col}' is categorical with {unique_counts[col]} unique values:")
    print(unique_values)

# Task 4: Compute summary statistics for numerical columns
numerical_columns = df.select_dtypes(include=['number'])


summary_stats = numerical_columns.describe()


mode = numerical_columns.mode().iloc[0]


print(summary_stats)
print("Mode:")
print(mode)

# Task 5: Compute summary statistics for categorical columns
categorical_summary_stats = df[categorical_columns].describe()


print(categorical_summary_stats)




# In[ ]:




