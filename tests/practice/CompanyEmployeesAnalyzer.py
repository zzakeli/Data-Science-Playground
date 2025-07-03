import pandas as pd

def create_dataframe():
    df = pd.DataFrame({
        'Name':['Mark','Rein','George','Miguel','Joseph'],
        'Department':['Transportation','Health','Transportation','Agriculture','Defense'],
        'Salary':[90000,50000,90000,30000,25000],
        'YearsAtCompany':[8,4,10,3,1]
        })

    return df

def compute_average_salary():
    df = create_dataframe()

    average_salary = df.Salary.mean()

    print('Average Employee Salary:', average_salary)

def compute_dept_average_salary():
    df = create_dataframe()
    average_salary = df.groupby('Department')['Salary'].mean()
    print('Average Department Salary:', average_salary)

def count_employees_per_dept():
    df = create_dataframe()

    dept_count = df.Department.value_counts()

    print(dept_count)

def define_seniority(x,df):
    i = 0
    if x > 3:
        df.at[i,'Seniority'] = 'Junior'
    if x >= 3 and x <= 6:
        df.at[i,'Seniority'] = 'Mid'
    else:
        df.at[i,'Seniority'] = 'Senior'

    i+=1

def add_column():
    df = create_dataframe()
    df['Seniority'] = None
    df.YearsAtCompany.map(lambda x: define_seniority(x,df))

    print(df)

def main():
    print()
    print(create_dataframe())
    print()
    compute_average_salary()
    print()
    compute_dept_average_salary()
    print()
    count_employees_per_dept()
    print()
    add_column()

if __name__ == "__main__":
    main()
