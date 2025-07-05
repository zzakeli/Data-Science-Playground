import pandas as pd

def init_dataframe():
    df = pd.DataFrame({
        'Name':['Erin','Vien','Katrina','Cath','George'],
        'Math':[92,75,85,65,90],
        'Science':[88,70,89,60,93],
        'English':[94,72,84,58,95],
        'Absences':[2,4,6,3,1],
        'Section':['Section A','Section B','Section A','Section C','Section B']
        })

    return df

def add_average_column():
    df = init_dataframe()
    df['Average'] = (df.Math + df.Science + df.English) / 3
    print(df)

def check_status(column):
    if column.Average >= 75 and column.Absences <= 5:
        return 'Passed'
    else:
        return 'Failed'

def add_status_column():
    df = init_dataframe()

    df['Average'] = (df.Math + df.Science + df.English) / 3

    df['Status'] = df.apply(check_status,axis=1)
    
    print(df)

def create_topper_column():
    df = init_dataframe()
    df['Average'] = (df.Math + df.Science + df.English) / 3

    max_average = df['Average'].max()
    df.loc[df.Average == max_average, 'Topper'] = 'Yes'
    df.loc[df.Average != max_average, 'Topper'] = 'No'

    print(df)

def check_remarks(average):
    if average >= 90:
        return 'Excellent'
    elif average >= 80 and average < 90:
        return 'Good'
    elif average >= 75 and average < 79:
        return 'Fair'
    else:
        return 'Poor'

def add_remarks():
    df = init_dataframe()
    df['Average'] = (df.Math + df.Science + df.English) / 3
    df['Remarks'] = df.Average.map(check_remarks)

    print(df)

def change_section(section):
    if section == 'Section A':
        return 'A'
    elif section == 'Section B':
        return 'B'
    else:
        return 'C'

def rename_section():
    df = init_dataframe()

    df['Section'] = df.Section.map(change_section)

    print(df)

def student_passed_summary():
    df = init_dataframe()

    df['Average'] = (df.Math + df.Science + df.English) / 3
    df['Status'] = df.apply(check_status,axis=1)

    section = df[df.Status == 'Passed'].groupby('Section')['Status'].count()
    print(section)

def main():
    print()
    add_average_column()
    print()
    add_status_column()
    print()
    create_topper_column()
    print()
    add_remarks()
    print()
    rename_section()
    print()
    student_passed_summary()

if __name__ == "__main__":
    main()
