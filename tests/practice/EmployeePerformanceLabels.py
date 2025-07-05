import pandas as pd

def init_dataframe():
    df = pd.DataFrame({
        'Employee':['John','Adam','Mich','Rogue','Fay'],
        'TaskCompleted':[45,20,50,30,25],
        'HoursWorked':[30,25,32,40,15],
        'Department':['Engineering','HR','Marketing','Engineering','Sales']
        })

    return df

def compute_efficiency(x):
    return x.TaskCompleted / x.HoursWorked
    

def create_eff_column():
    df = init_dataframe()

    df['Efficiency'] = df.apply(compute_efficiency, axis=1)

    print(df)

def check_performance(efficiency):
    if efficiency >= 1.5:
        return 'Excellent'
    elif efficiency < 1.5 and efficiency >= 1:
        return 'Good'
    else:
        return 'Needs Improvement'

def create_performance_column():
    df = init_dataframe()

    df['Efficiency'] = df.apply(compute_efficiency,axis=1)

    df['Performance'] = df.Efficiency.map(check_performance)

    print(df)

def apply_bonus(column):
    if column.Efficiency >= 1.5:
        return 2000
    elif column.Efficiency >= 1 and column.Efficiency < 1.5:
        return 1000
    else:
        return 0

def create_bonus_column():
    df = init_dataframe()

    df['Efficiency'] = df.apply(compute_efficiency,axis=1)

    df['Bonus'] = df.apply(apply_bonus,axis=1)

    print(df)

def convert(department):
    if department == 'HR':
        return 'H'
    elif department == 'Engineering':
        return 'E'
    elif department == 'Marketing':
        return 'M'
    else:
        return 'X'

def convert_to_codes():
    df = init_dataframe()
    df.Department = df.Department.map(convert)
    print(df)

def main():
    print()
    create_eff_column()
    print()
    create_performance_column()
    print()
    create_bonus_column()
    print()
    convert_to_codes()
    print()
if __name__ == "__main__":
    main()

