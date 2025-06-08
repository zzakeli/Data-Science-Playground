import pandas as pd

#CREATING DATA
#two core objects in pandas are the DataFrame and the Series.

def createDataFrame():
	df = pd.DataFrame({'Bob': ['I like it', 'It was awful'],
			'Sue': ['Pretty good','Bland']}, index =['Product A','Product B'])
	print(df)

def createSeries():
    se = pd.Series([1,2,3,4,5], index=[2020, 2021, 2022, 2023, 2024], name="Product A")
    print(se)

def readExcel():
    df_sample = pd.read_excel("../../Creating Reading and Writing Data/datasets/sample.xlsx")
    size = df_sample.shape
    head = df_sample.head()
    print()
    print("DataFrame size: ", size)
    print()
    print("Head:")
    print(head)
    print()
    print(df_sample)
    print()

readExcel()
#createSeries()
#createDataFrame()
