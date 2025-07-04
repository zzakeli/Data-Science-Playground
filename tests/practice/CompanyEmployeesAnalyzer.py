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

def define_seniority(x):
    if x < 3:
        return 'Junior'
    if x >= 3 and x <= 6:
        return 'Mid'
    else:
        return 'Senior'


def add_column():
    df = create_dataframe()
    df['Seniority'] = None
    df['Seniority'] = df.YearsAtCompany.map(define_seniority)

    print(df)

def add_tax_column():
    df = create_dataframe()
    df['Tax'] = df.Salary.map(lambda salary: salary * 0.15)
    print(df)

def summary():
    df = create_dataframe()

    print('Summary')
    print('Total no. of Employees:', df.Name.count())
    print('Average years at Company:', df.YearsAtCompany.mean())
    print('Total Salary Expense:', df.Salary.sum())

def show_dept_highest_average_salary():
    df = create_dataframe()

    print('Department with highest average salary:',df.groupby('Department')['Salary'].mean().idxmax())

def main():
    print('-----------------------------------------------------------')
    print(create_dataframe())
    print('-----------------------------------------------------------')
    compute_average_salary()
    print('-----------------------------------------------------------')
    compute_dept_average_salary()
    print('-----------------------------------------------------------')
    count_employees_per_dept()
    print('-----------------------------------------------------------')
    add_column()
    print('-----------------------------------------------------------')
    add_tax_column()
    print('-----------------------------------------------------------')
    summary()
    print('-----------------------------------------------------------')
    show_dept_highest_average_salary()
    print('-----------------------------------------------------------')

if __name__ == "__main__":
    main()
