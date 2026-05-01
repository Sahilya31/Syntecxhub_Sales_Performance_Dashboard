import pandas as pd
import random
from datetime import datetime, timedelta

brands = ["Nike", "Adidas", "Puma", "Reebok", "Under Armour", "Zara", "H&M"]
products = ["Shoes", "Tshirt", "Cap"]
regions = ["Mumbai", "Delhi", "Bangalore"]

data = []

start_date = datetime(2023, 1, 1)

for i in range(500):   # 👈 yaha 500 rows (tu 1000 bhi kar sakta hai)
    date = start_date + timedelta(days=random.randint(0, 200))
    brand = random.choice(brands)
    product = random.choice(products)
    region = random.choice(regions)

    sales = random.randint(100000, 1000000)  # 👈 Lakhs range

    quantity = random.randint(1, 5)

    data.append([date, brand, product, "Fashion", sales, quantity, region])

df = pd.DataFrame(data, columns=[
    "Order_Date", "Brand", "Product", "Category", "Sales", "Quantity", "Region"
])

df.to_csv("sales_data.csv", index=False)

print("✅ Large dataset generated!")