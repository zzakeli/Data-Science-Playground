import pandas as pd

def create_dataframe():
    df = pd.DataFrame(
            {
                'Name':['John','Justin','Eric','Ann','Mary'],
                'Math':[90,88,96,85,88],
                'Science':[90,90,89,92,94],
                'English':[94,96,96,92,93]
                }
            )

    return df

def show_first_three_student_scores():
    df = create_dataframe()

    scores = df.iloc[:3,:]
    print(scores)

def show_science_score():
    df = create_dataframe()

    person_record = df.loc[df.Name == 'Ann']
    science_score = person_record['Science']
    print(science_score)

def change_score():
    df = create_dataframe()

    df.iloc[1,1] = 95

    print(df)

def change_english_score():
    df = create_dataframe()

    df.loc[df.Name == 'Mary', 'English'] = 88

    print(df)

def create_column():
    df = create_dataframe()

    #row = 5
    #col = 4print
    #passed = []
    #for i in range(row):
    #    sum = 0
    #    for j in range(col - 1):
    #        sum += df.iloc[i,j + 1]

    #    average = sum/(col - 1)

    #    if average >= 75:
     #       passed.append("Yes")
     #   else:
    #        passed.append("No")

    df.loc[((df.Math + df.Science + df.English) / 3) >= 90,'Passed'] = 'Yes'
    df.loc[((df.Math + df.Science + df.English) / 3) < 90, 'Passed'] = 'No'

    print(df)

def show_two_last_students():
    df = create_dataframe()

    print(df.iloc[3:,1::2])

#not done yet
def show_topper():
    df = create_dataframe()
    row = 5
    col = 4
    #top = df.iloc[0,1]
    for i in range(row):
        sum = 0
        for j in range(col - 1):
            sum += df.iloc[i, j + 1]

        average = sum / (col - 1)

    df.loc[average == top,'Topper'] = 'Yes'
    df.loc[average != top,'Topper'] = 'No'
    print(df)

def main():
    print(create_dataframe())
    print()
    show_first_three_student_scores()
    print()
    show_science_score()
    print()
    change_score()
    print()
    change_english_score()
    print()
    create_column()
    print()
    show_two_last_students()
    print()
    show_topper()


if __name__ == "__main__":
    main()
