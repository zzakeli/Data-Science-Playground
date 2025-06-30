import pandas as pd

df = pd.DataFrame(
        {'country':['Italy','Portugal','France'],
         'description':['desc1','desc2','desc3'],
         'points':[87,87,90],
         'price':[12,15.0,32.0],
         'province':['Sicily & Sardinia','Douro','Alsace']}
        )

def showDataFrame():
    print(df)


def loop(x):
    df_mean = df.points.mean()
    return x - df_mean

def mapColumns():
    print(df.points.map(loop))

mapColumns()

#print(df.corr()) #correlation works only if values inside the dataframe are numeric
#print(df.points.mode())
#print(df.points.median())
#print(df.points.value_counts())
#print(df.price.mean())
#print(df.points.unique())
#print(df.country.describe())
#print(df.points.describe())
