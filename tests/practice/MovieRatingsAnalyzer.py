import pandas as pd

def create_dataframe():
    df = pd.DataFrame({
        'Title':['Spiderman','The 100','Avatar','John Wick','World War Z'],
        'Genre':['Fantasy','Adventure','Adventure','Action','Horror'],
        'Year':[2009,2014,2018,2024,2018],
        'Rating':[9.2,10,8.7,5,7.5]
        })

    return df

def display_movie_released():
    df = create_dataframe()
    
    movies = df.loc[df.Year > 2015]

    print(movies)

def average_rating():
    df = create_dataframe()
    row = 5
    col = 4

    sum = 0
    for i in range(row):
        sum += df.iloc[i,col - 1]

    average = sum/row
    print(average)


print()
print(create_dataframe())
print()
display_movie_released()
print()
average_rating()

