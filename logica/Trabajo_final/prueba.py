# Importing pandas package
import pandas as pd

# Importing methods from tabulate
from tabulate import tabulate

# Creating a dictionary
d = {
    'A':['Madhya Pradesh','Rajasthan','Gujrat','Punjab'],
    'B':['Bhopal','Jaipur','Gandhinagar','Chandigarh']
}

# Creating DataFrame
df = pd.DataFrame(d)

# Display the DataFrame
print("Original DataFrame:\n",df,"\n")

# Display DataFrame in using tabulate
df.sort_values(ascending = False)
print("DataFrame using tabulate:\n")
print(tabulate(df, showindex=False, headers=['States','Capitals']))
