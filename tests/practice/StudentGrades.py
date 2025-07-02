import pandas as pd

def create_dataframe():
    df = pd.DataFrame({
        'Name':['John','Murphy','Ann','Cassy','Justin'],
        'Math':[88,94,92,85,96],
        'Science':[90,90,91,92,91],
        'English':[98,92,90,92,90]
        })
    return df

def get_first_row():
    df = create_dataframe()
    
    #first_five_rows = df.head()
    first_row = df.iloc[0,:]
    print(first_row)

def create_column():
    df = create_dataframe()

    average_list = []
    row = 5
    col = 4

    for i in range(row):
        sum = 0
        for j in range(col - 1):
            sum += df.iloc[i,j + 1]
        average_list.append(sum/(col - 1))

    df['Average'] = average_list
    print(df)

create_column()
