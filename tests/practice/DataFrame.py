import pandas as pd

df = pd.DataFrame({'category_name': ['Salary','Rent'],'category_type': ['Income','Expense']},index=['category_1','category_2'])


def createDataFrame():
    df = pd.DataFrame({'category_name': ['Salary', 'Rent'],'category_type': ['Income','Expense'] },index=['category_1','category_2'])
    print(df)

def selectIncomeOnly():
    #print(df.loc[df.category_type == 'Income'])
    print(df.iloc[1:])

#createDataFrame()
selectIncomeOnly()
