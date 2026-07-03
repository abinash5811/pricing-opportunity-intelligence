import pandas as pd
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"
DATA_DIR.mkdir(exist_ok=True)

regions = pd.DataFrame([
    [1, "North America", "Americas"],
    [2, "EMEA", "Europe/Middle East/Africa"],
    [3, "APAC", "Asia Pacific"],
    [4, "LATAM", "Latin America"],
], columns=["region_id", "region_name", "market"])

products = pd.DataFrame([
    [1, "Learning Pro", "Learning", "Pro", 12000],
    [2, "Learning Enterprise", "Learning", "Enterprise", 25000],
    [3, "Recruiter Pro", "Recruiting", "Pro", 18000],
    [4, "Sales Navigator", "Sales", "Enterprise", 22000],
    [5, "Marketing Advanced", "Marketing", "Enterprise", 30000],
], columns=["product_id", "product_name", "product_family", "package_type", "list_price"])

account_managers = pd.DataFrame([
    [i, f"Account Manager {i}", random.choice(regions["region_name"].tolist()), random.choice(["AE", "Senior AE", "Sales Manager"])]
    for i in range(1, 31)
], columns=["account_manager_id", "account_manager_name", "manager_region", "role_title"])

contract_types = pd.DataFrame([
    [1, "Annual", "One year contract"],
    [2, "Multi-Year", "Two or three year contract"],
    [3, "Trial", "Short trial contract"],
], columns=["contract_type_id", "contract_type_name", "description"])

opportunity_stages = pd.DataFrame([
    [1, "Prospecting", 1, "Open"],
    [2, "Proposal", 2, "Open"],
    [3, "Negotiation", 3, "Open"],
    [4, "Closed Won", 4, "Closed"],
    [5, "Closed Lost", 5, "Closed"],
], columns=["stage_id", "stage_name", "stage_order", "stage_category"])

industries = ["Technology", "Finance", "Healthcare", "Education", "Retail", "Manufacturing"]
segments = ["Enterprise", "Mid-Market", "SMB"]
company_sizes = ["Small", "Medium", "Large", "Strategic"]

customers = []
for i in range(1, 2001):
    seats = random.randint(50, 5000)
    utilization = random.randint(35, 100)
    customers.append([
        i,
        f"Customer_{i}",
        random.choice(regions["region_id"].tolist()),
        random.choice(industries),
        random.choice(segments),
        random.choice(company_sizes),
        seats,
        utilization
    ])

customers = pd.DataFrame(customers, columns=[
    "customer_id", "customer_name", "region_id", "industry", "segment",
    "company_size", "current_seats", "seat_utilization_percent"
])

start_date = date(2025, 1, 1)
dates = []
for i in range(365):
    d = start_date + timedelta(days=i)
    dates.append([i + 1, d, d.day, d.month, (d.month - 1) // 3 + 1, d.year, d.strftime("%A")])

dim_date = pd.DataFrame(dates, columns=["date_id", "full_date", "day", "month", "quarter", "year", "day_name"])

opportunities = []
for i in range(1, 12001):
    customer_id = random.randint(1, 2000)
    product_id = random.randint(1, 5)
    am_id = random.randint(1, 30)
    stage_id = random.randint(1, 5)
    contract_type_id = random.randint(1, 3)
    expected_value = random.randint(10000, 250000)
    probability = random.randint(10, 95)
    created = start_date + timedelta(days=random.randint(0, 300))
    renewal = created + timedelta(days=random.randint(30, 180))

    opportunities.append([
        i, customer_id, product_id, am_id, stage_id, contract_type_id,
        random.choice(["New", "Renewal", "Expansion"]),
        expected_value, probability, renewal, created
    ])

opportunities = pd.DataFrame(opportunities, columns=[
    "opportunity_id", "customer_id", "product_id", "account_manager_id",
    "stage_id", "contract_type_id", "opportunity_type", "expected_value",
    "probability_percent", "renewal_date", "created_date"
])

quotes = []
for i in range(1, 12001):
    opp = opportunities.iloc[i - 1]
    product = products[products["product_id"] == opp["product_id"]].iloc[0]
    list_price = product["list_price"]
    discount = random.randint(0, 55)
    quoted_price = list_price * (1 - discount / 100)

    quotes.append([
        i,
        int(opp["opportunity_id"]),
        list_price,
        round(quoted_price, 2),
        discount,
        random.choice(["Draft", "Approved", "Rejected", "Accepted"]),
        opp["created_date"] + timedelta(days=random.randint(1, 20))
    ])

quotes = pd.DataFrame(quotes, columns=[
    "quote_id", "opportunity_id", "list_price", "quoted_price",
    "discount_percent", "quote_status", "quote_date"
])

contracts = []
for i in range(1, 8001):
    customer_id = random.randint(1, 2000)
    product_id = random.randint(1, 5)
    am_id = random.randint(1, 30)
    contract_type_id = random.randint(1, 3)
    start = start_date + timedelta(days=random.randint(0, 250))
    term = random.choice([12, 24, 36])
    end = start + timedelta(days=term * 30)
    value = random.randint(15000, 300000)

    contracts.append([
        i, customer_id, product_id, am_id, contract_type_id,
        start, end, value, term, random.choice([True, False])
    ])

contracts = pd.DataFrame(contracts, columns=[
    "contract_id", "customer_id", "product_id", "account_manager_id",
    "contract_type_id", "contract_start_date", "contract_end_date",
    "contract_value", "contract_term_months", "is_renewal"
])

bookings = []
for i in range(1, 20001):
    contract = contracts.iloc[random.randint(0, len(contracts) - 1)]
    booking_date = contract["contract_start_date"] + timedelta(days=random.randint(0, 60))

    bookings.append([
        i,
        int(contract["contract_id"]),
        int(contract["customer_id"]),
        int(contract["product_id"]),
        booking_date,
        random.randint(5000, 150000),
        random.choice(["Completed", "Pending", "Cancelled"])
    ])

bookings = pd.DataFrame(bookings, columns=[
    "booking_id", "contract_id", "customer_id", "product_id",
    "booking_date", "booking_amount", "booking_status"
])

usage = []
for i in range(1, 50001):
    customer = customers.iloc[random.randint(0, len(customers) - 1)]
    product_id = random.randint(1, 5)
    licensed = int(customer["current_seats"])
    active = random.randint(10, licensed)
    utilization = round((active / licensed) * 100, 2)

    usage.append([
        i,
        int(customer["customer_id"]),
        product_id,
        start_date + timedelta(days=random.randint(0, 364)),
        active,
        licensed,
        utilization
    ])

usage = pd.DataFrame(usage, columns=[
    "usage_id", "customer_id", "product_id", "usage_date",
    "active_users", "licensed_seats", "utilization_percent"
])

tables = {
    "dim_region.csv": regions,
    "dim_product.csv": products,
    "dim_account_manager.csv": account_managers,
    "dim_contract_type.csv": contract_types,
    "dim_opportunity_stage.csv": opportunity_stages,
    "dim_customer.csv": customers,
    "dim_date.csv": dim_date,
    "fact_opportunity.csv": opportunities,
    "fact_quote.csv": quotes,
    "fact_contract.csv": contracts,
    "fact_booking.csv": bookings,
    "fact_usage.csv": usage,
}

for filename, df in tables.items():
    df.to_csv(DATA_DIR / filename, index=False)

print("EPAP enterprise dataset generated successfully.")
for filename, df in tables.items():
    print(f"{filename}: {len(df)} rows")