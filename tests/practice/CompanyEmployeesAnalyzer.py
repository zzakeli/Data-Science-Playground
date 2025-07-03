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

    print('Average Department Salary:', average_salary)
def main():
    print()
    print(create_dataframe())
    print()
    compute_average_salary()
    print()
    compute_dept_average_salary()
    print()

if __name__ == "__main__":
    main()
