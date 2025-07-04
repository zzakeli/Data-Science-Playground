import pandas as pd

"""
This code provides CLI simulation of an Online Store Analysis.
Dynamic approach to strengthen data analysis skills.

This code doesn't have generic edge cases, it demonstrates the
dynamic purpose of the code dynamically.
"""

def initialize_dataframe():
    df = pd.DataFrame({
        'Customer':['Eden','John','Ann','Michael','Jack'],
        'Product':['Phone','Mango','Rice','Book','Laptop'],
        'Category':['Electronics','Food','Food','Supplies','Electronics'],
        'Price':[7000,250,530,1500,30000],
        'Quantity':[1,4,2,2,1],
        'Country':['China','Philippines','China','US','US']
        })

    return df

def create_dataframe():
    row = int(input("Enter number of Customer:"))

    df = pd.DataFrame()
    customer = []
    product = []
    category = []
    price = []
    quantity = []
    country = []

    for i in range(row):
        customer.append(input("Enter customer name: "))
        product.append(input(f"Enter {customer[i]}'s product: "))
        category.append(input("Enter category: "))
        price.append(int(input(f"Enter {product[i]}'s price: ")))
        quantity.append(int(input("Enter quantity: ")))
        country.append(input("Enter country: "))

    df['Customer'] = customer
    df['Product'] = product
    df['Category'] = category
    df['Price'] = price
    df['Quantity'] = quantity
    df['Country'] = country

    return df

def is_big_spender(revenue):
    if revenue > 1000:
        return 'Yes'
    else:
        return 'No'


def compute_total_revenue(df):
    df['Revenue'] = df['Price'] * df['Quantity']
    print('Generated Total Revenue Table:')
    print(df)
    
def find_average_revenue(df):
    df['Revenue'] = df['Price'] * df['Quantity']
    print('Average Revenue Per Country:')
    print(df.groupby('Country')['Revenue'].mean())
    
def count_product_sold(df):
    print('Product Sold per Category:')
    print(df.groupby('Category')['Quantity'].sum())
    
def add_big_spender_column(df):
    df['Revenue'] = df['Price'] * df['Quantity']
    df['BigSpender'] = df.Revenue.map(is_big_spender)

    print('Generated Table w/ BigSpender Column:')
    print(df)
    
def add_tax_column(df):
    df['Revenue'] = df['Price'] * df['Quantity']
    df['Tax'] = df['Revenue'] * 0.12

    print("Generated Table w/ Tax Column:")
    print(df)
    
def get_total_revenue_generated(df):
    country = input("Enter a country: ")
    df['Revenue'] = df['Price'] * df['Quantity']

    print(f"Total Revenue Generated for {country}:",df.groupby("Country")['Revenue'].sum().get(country,0))
    
def find_highest_average_order_revenue(df):
    df['Revenue'] = df['Price'] * df['Quantity']
    print('Country w/ Highest Average Revenue:',df.groupby('Country')['Revenue'].mean().idxmax())
    



def main():
    df = initialize_dataframe()
    #df = create_dataframe()

    while True:
        df = initialize_dataframe()
        print("""
        SELECT CHOICES
        [1] COMPUTE TOTAL REVENUE
        [2] FIND AVERAGE REVENUE PER COUNTRY
        [3] COUNT PRODUCTS SOLD IN EACH CATEGORY
        [4] ADD BIG SPENDER COLUMN
        [5] ADD TAX COLUMN
        [6] GET TOTAL REVENUE GENERATED
        [7] FIND COUNTRY WITH HIGHEST AVERAGE ORDER REVENUE
        [0] EXIT
          """)
        choice = input("ENTER HERE: ")
        print()
        if choice == '0':
            print("Exiting...")
            break
        elif choice == '1':
            compute_total_revenue(df)
        elif choice == '2':
            find_average_revenue(df)
        elif choice == '3':
            count_product_sold(df)
        elif choice == '4':
            add_big_spender_column(df)
        elif choice == '5':
            add_tax_column(df)
        elif choice == '6':
            get_total_revenue_generated(df)
        elif choice == '7':
            find_highest_average_order_revenue(df)
        else:
            print("Invalid Prompt. Try Again.")


if __name__ == "__main__":
    main()
