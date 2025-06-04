import pandas as pd

df = pd.DataFrame({"Name":["John","Mary"],"Age":[20,24], "Gender": ["Male","Female"]})

def selectingData():
    print(df['Age'][0])
    print()
    print(df['Gender'][1])

def indexingData():
    #print(df.iloc[:,:])
    print(df.loc[:, 'Age'])

def manipulatingIndex():
    idf = df.set_index("Name")
    print(idf.loc['John'])

def conditionalSelection():
    #print(df.loc[df.Gender == "Male"])
    #print(df.loc[df.Age > 21])
    print(df.loc[(df.Gender == "Male") | (df.Gender == "Female")])

def assigningData():
    df["Name"] = "Paul"
    print(df)
#selectingData()
#indexingData()
#manipulatingIndex()
#conditionalSelection()
assigningData()
