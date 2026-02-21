from faker import Faker
import random
import time
import pymongo
from typing import Tuple


fake = Faker()

def connect():
    client = pymongo.MongoClient(
        "mongodb+srv://<username>:<password>@cluster0.7v8ytwp.mongodb.net/?appName=Cluster0"
    )
    return client["insurance"]


def create_data() -> Tuple[dict, dict]:
    customer = {
        "customer_id": f"CUST-{random.randint(100, 999)}",
        "name": fake.name(),
        "state": fake.state_abbr(),
        "policy_type": random.choice(["Auto", "Home", "Health"])
    }

    claim = {
        "claim_id": f"CLM-{random.randint(1000, 9999)}",
        "customer_id": customer["customer_id"],
        "date": fake.date_between(start_date='-1y', end_date='today').isoformat(),
        "amount": round(random.uniform(100, 20000), 2),
        "claim_type": random.choice(["Accident", "Theft", "Fire"]),
        "is_fraud": random.random() < 0.05
    }

    return customer, claim


def insert_data(db, customer: dict, claim: dict):
    customers_col = db["customers"]
    claims_col = db["claims"]

    customers_col.insert_one(customer)
    claims_col.insert_one(claim)

    print(f"Inserted claim {claim['claim_id']} for customer {customer['customer_id']}")


if __name__ == "__main__":
    db = connect()

    if db is not None:
        while True:  # Simulates streaming data
            customer, claim = create_data()
            insert_data(db, customer, claim)
            time.sleep(2)  # Inserts every 2 seconds
