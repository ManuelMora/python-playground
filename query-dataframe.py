import pandas as pd

data = pd.read_csv("employees.csv")
data.columns = [column.replace(" ", "_") for column in data.columns]

data.query(
    'Senior_Management==True and Gender=="Male" and Team=="Marketing" and First_Name=="Johnny"',
    inplace=True,
)

print(data.loc[413, "Gender"])
