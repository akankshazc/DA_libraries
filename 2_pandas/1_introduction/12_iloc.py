import pandas as pd

# cretae a dataframe
data = {'Name': ['SecUnit', 'Mensah', 'Ratthi', 'Pin-lee', 'Gurathin', 'Bharadwaj', 'Volescu'],
        'Age': [4, 40, 30, 35, 35, 45, 50],
        'Occupation': ['Security', 'Team Leader', 'Biology Specialist', 'Lawyer', 'Systems Specialist', 'Scientist', 'Scientist'], }

df = pd.DataFrame(data)

# get second row
second_row = df.iloc[1]

print(second_row)
