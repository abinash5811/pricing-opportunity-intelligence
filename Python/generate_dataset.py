import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

regions = ["North America", "EMEA", "APAC", "LATAM"]
industries = ["Technology", "Finance", "Healthcare", "Education", "Retail"]
segments = ["Enterprise", "Mid-Market", "SMB"]
stages = ["Prospecting", "Proposal", "Negotiation", "Closed Won", "Closed Lost"]
products = ["Learning Pro", "Recruiter Pro", "Sales Navigator", "Marketing Solutions"]

customers = []

for i in range(1, 201):
    customers.append({
        "customer_id": i,
        "customer_name": f"Customer_{i}",
        "region": random.choice(regions),
        "industry": random.choice(industries),
        "segment": random.choice(segments),
        "current_seats": random.randint(50, 5000),
        "seat_utilization_percent": random.randint(40, 100)
    })

customers_df = pd.DataFrame(customers)

opportunities = []

for i in range(1, 401):
    customer_id = random.randint(1, 200)
    renewal_date = datetime.today() + timedelta(days=random.randint(1, 180))

    opportunities.append({
        "opportunity_id": i,
        "customer_id": customer_id,
        "stage": random.choice(stages),
        "renewal_date": renewal_date.strftime("%Y-%m-%d"),
        "contract_term_months": random.choice([12, 24, 36]),
        "account_manager": f"AM_{random.randint(1, 20)}"
    })

opportunities_df = pd.DataFrame(opportunities)

pricing = []

for i in range(1, 201):
    list_price = random.randint(10000, 200000)
    discount_percent = random.randint(0, 55)
    current_price = list_price * (1 - discount_percent / 100)

    pricing.append({
        "customer_id": i,
        "list_price": list_price,
        "current_price": round(current_price, 2),
        "discount_percent": discount_percent,
        "annual_contract_value": round(current_price, 2)
    })

pricing_df = pd.DataFrame(pricing)

bookings = []

for i in range(1, 1001):
    customer_id = random.randint(1, 200)
    booking_date = datetime.today() - timedelta(days=random.randint(1, 365))

    bookings.append({
        "booking_id": i,
        "customer_id": customer_id,
        "product_name": random.choice(products),
        "booking_amount": random.randint(5000, 100000),
        "booking_date": booking_date.strftime("%Y-%m-%d"),
        "status": random.choice(["Completed", "Pending", "Cancelled"])
    })

bookings_df = pd.DataFrame(bookings)

customers_df.to_csv("data/customers.csv", index=False)
opportunities_df.to_csv("data/opportunities.csv", index=False)
pricing_df.to_csv("data/pricing.csv", index=False)
bookings_df.to_csv("data/bookings.csv", index=False)

print("Dataset created successfully.")
print("Files created:")
print("- data/customers.csv")
print("- data/opportunities.csv")
print("- data/pricing.csv")
print("- data/bookings.csv")