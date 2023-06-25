from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta

fake = Faker()

# Generate Customers Table
customers = []
for _ in range(60):
    customer_id = fake.unique.random_int(min=1000, max=9999)
    name = fake.name()
    gender = random.choice(['Male', 'Female'])
    age = random.randint(18, 65)
    country = fake.country()
    region = fake.random_int(min=1, max=10)
    customers.append((customer_id, name, gender, age, country, region))

# Generate Products Table
products = []
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports']
for _ in range(30):
    product_id = fake.unique.random_int(min=100, max=999)
    name = fake.word()
    price = random.uniform(10, 100)
    category = random.choice(categories)
    products.append((product_id, name, price, category))

# Generate Orders Table
orders = []
start_date = datetime.now() - timedelta(days=365)
for _ in range(100):
    order_id = fake.unique.random_int(min=10000, max=99999)
    customer_id = random.choice(customers)[0]
    order_date = fake.date_time_between(start_date=start_date, end_date='now')
    delivery_date = order_date + timedelta(days=random.randint(1, 10))
    orders.append((order_id, customer_id, order_date, delivery_date))

# Generate OrderItems Table
order_items = []
for order in orders:
    order_id = order[0]
    product_id = random.choice(products)[0]
    price = random.uniform(10, 100)
    quantity = random.randint(1, 10)
    order_items.append((order_id, product_id, price, quantity))


# Convert data to pandas DataFrames
customers_df = pd.DataFrame(customers, columns=['customer_id', 'name', 'gender', 'age', 'country', 'region'])
products_df = pd.DataFrame(products, columns=['product_id', 'name', 'price', 'category'])
orders_df = pd.DataFrame(orders, columns=['order_id', 'customer_id', 'order_date', 'delivery_date'])
order_items_df = pd.DataFrame(order_items, columns=['order_id', 'product_id', 'price', 'quantity'])

# Save data to Excel file
with pd.ExcelWriter('online_retail_sales_data.xlsx') as writer:
    customers_df.to_excel(writer, sheet_name='Customers', index=False)
    products_df.to_excel(writer, sheet_name='Products', index=False)
    orders_df.to_excel(writer, sheet_name='Orders', index=False)
    order_items_df.to_excel(writer, sheet_name='OrderItems', index=False)

print("Data saved to Excel file successfully.")






