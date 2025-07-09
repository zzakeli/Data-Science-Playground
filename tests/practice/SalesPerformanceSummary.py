import pandas as pd

"""
Which store made the most money?
Which category performed best overall?
Which product was the top-seller in each category?
How do sales change month-to-month?
"""
def main():
    df = pd.DataFrame({
        'store_id':[1,2,1,2,3],
        'category':['Beverage','Snack','Beverage','Snack','Produce'],
        'product':['Cola','Chips','Juice','Crackers','Apples'],
        'date':['2024-01-05','2024-01-05','2024-01-06','2024-01-06','2024-01-06'],
        'units_sold':[100,60,120,50,200],
        'unit_price':[1.25,0.75,1.50,0.80,0.50]
        })

    df['total_sales'] = df['units_sold'] * df['unit_price']
    print(df)

    print(df.groupby('store_id')[['units_sold','total_sales']].agg('sum'))

    df['average_sales'] = df['total_sales'].mean()
    print(df.groupby('category')[['units_sold','total_sales','average_sales']].agg('sum'))

    top_prod = df.loc[df.groupby('category')['units_sold'].idxmax()]
    print(top_prod[['category', 'product']])


if __name__ == '__main__':
    main()
