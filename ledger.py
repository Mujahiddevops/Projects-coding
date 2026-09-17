# Client Ledger and Outstanding Balance Tracker

def format_currency(amount):
    return f"KES {amount:,.2f}"

def generate_reminder(client_name, balance):
    return f"Hello {client_name}, kindly note you have an outstanding balance of {format_currency(balance)}."

def process_ledger(clients):
    total_outstanding = 0
    print("=== CLIENT OUTSTANDING BALANCES ===")
    
    for client in clients:
        balance = client["total_due"] - client["paid"]
        if balance > 0:
            total_outstanding += balance
            print(f"⚠️  {client['name']}")
            print(f"    Balance: {format_currency(balance)}")
            print(f"    Message: \"{generate_reminder(client['name'], balance)}\"\n")
        else:
            print(f"✅ {client['name']} is fully paid up.\n")
            
    print(f"Total Portfolio Outstanding: {format_currency(total_outstanding)}")
    return total_outstanding

if __name__ == "__main__":
    sample_clients = [
        {"name": "A & A Cosmetics", "total_due": 150000, "paid": 100000},
        {"name": "Nexus Logistics", "total_due": 85000, "paid": 85000},
        {"name": "Safari Traders", "total_due": 200000, "paid": 120000},
    ]
    process_ledger(sample_clients)

