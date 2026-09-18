import csv
import os

def record_transaction(client_name, service, amount, filename="deals.csv"):
    file_exists = os.path.exists(filename)
    with open(filename, mode="a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Client", "Service", "Amount"])
        writer.writerow([client_name, service, amount])

if __name__ == "__main__":
    record_transaction("Sample Client", "DevOps Setup", 250.0)
    print("Transaction recorded successfully!")
