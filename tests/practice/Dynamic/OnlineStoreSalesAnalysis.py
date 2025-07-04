import pandas as pd

"""
This code provides CLI implementation of an Online Store Analysis.
Dynamic approach to strengthen data analysis skills.
"""

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

def main():
    df = create_dataframe()


if __name__ == "__main__":
    main()
