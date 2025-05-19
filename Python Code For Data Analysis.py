#uploading all the necessary library modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import the dataset and viewing the data
data = '/Users/dhruvkarande/Documents/Data Analytics Project /Green House Plant Growth/Greenhouse Plant Growth Metrics.csv'
df = pd.read_csv(data)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# show first 5 and last 5 rows
print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#understanding the data in the dataset
print(df.columns)
print(df["Random"].unique())
print(df["Class"].unique())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#cleaning data
df = df.dropna()
net_null = df.notnull().sum()
print(net_null)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#data correlation
# Step 1: Convert 'Random' and 'Class' to numeric manually using Pandas
df['Random'] = df['Random'].astype('category').cat.codes
df['Class'] = df['Class'].astype('category').cat.codes

#make set of columns you want to find the correlation between
set = ['Random', 'ACHP', 'PHR', 'AWWGV', 'ALAP', 'ANPL', 'ARD', 'ADWR', 'PDMVG', 'ARL', 'AWWR', 'ADWV', 'PDMRG', 'Class']

#apply correlation
corr_matrix = df[set].corr()

print('Correlation Matrix')
print(corr_matrix.to_string())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from math import ceil

# Get unique number of classes and random values
num_classes = df['Class'].nunique()
num_randoms = df['Random'].nunique()

# Create a grid for plotting (rows = classes, columns = randoms)
fig, axes = plt.subplots(num_classes, num_randoms, figsize=(num_randoms * 6, num_classes * 4))
fig.suptitle("Mean Value Bar Charts for Each Class-Random Combination", fontsize=16)

# Loop through each class and random value
for class_val in range(num_classes):
    for random_val in range(num_randoms):
        # Filter rows
        filtered_df = df[(df['Class'] == class_val) & (df['Random'] == random_val)]
        if filtered_df.empty:
            continue

        # Compute mean values
        mean_vals = filtered_df.drop(columns=['Class', 'Random']).mean()

        # Compute subplot position
        row = class_val

        # Bar chart
        mean_vals.plot(kind='bar', ax=axes[row][random_val], color='skyblue', edgecolor='black')
        axes[row][random_val].set_title(f'Bar: Class={class_val}, Random={random_val}', fontsize=10)
        axes[row][random_val].tick_params(axis='x', labelrotation=45)

plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.show()
