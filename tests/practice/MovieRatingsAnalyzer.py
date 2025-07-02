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
    print('Average Rating:',average)

def showActionMovies():
    df = create_dataframe()
    action_movies = df.loc[(df['Genre'] == 'Action') & (df['Rating'] >= 8)]

    print(action_movies)

def sort_descending():
    df = create_dataframe()
    sorted = df.sort_values(by='Rating', ascending=False)
    
    print(sorted)

def add_recommendation():
    df = create_dataframe()

    recommendation = []
    row = 5
    col = 4
    for i in range(row):
        rating = df.iloc[i, col - 1]
        if rating >= 7.5:
            recommendation.append('Yes')
        else:
            recommendation.append('No')

    df['Recommended'] = recommendation

    print(df)


print()
print(create_dataframe())
print()
display_movie_released()
print()
average_rating()
print()
showActionMovies()
print()
sort_descending()
print()
add_recommendation()
