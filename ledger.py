# ledger.py - Client Expense & Balance Tracker

def generate_ledger_summary(client_name, initial_balance, transactions):
    current_balance = initial_balance
    summary_lines = [f"--- Ledger Summary for {client_name} ---"]
    summary_lines.append(f"Starting Balance: KES {initial_balance:,.2f}\n")
    
    summary_lines.append("Transactions:")
    for desc, amount in transactions:
        current_balance += amount
        type_str = "Payment Received" if amount < 0 else "Charge Added"
        summary_lines.append(f" - {desc}: KES {abs(amount):,.2f} ({type_str})")
        
    summary_lines.append(f"\nFinal Outstanding Balance: KES {current_balance:,.2f}")
    
    # Generate WhatsApp-ready reminder snippet
    whatsapp_msg = (
        f"\n*Payment Reminder for {client_name}*\n"
        f"Hello! Your current ledger balance is *KES {current_balance:,.2f}*.\n"
        f"Please review your statement and let us know if you have any questions."
    )
    
    return "\n".join(summary_lines), whatsapp_msg


if __name__ == "__main__":
    client = "Acme Media"
    starting_amt = 15000.00
    
    # Positive values = charges, Negative values = payments received
    tx_history = [
        ("Script Writing Service", 5000.00),
        ("Advance Payment", -10000.00),
        ("Video Editing Add-on", 3500.00)
    ]
    
    report, reminder = generate_ledger_summary(client, starting_amt, tx_history)
    
    print(report)
    print("\n" + "="*40)
    print("WhatsApp Card Preview:")
    print("="*40)
    print(reminder)
# ledger.py - Client Expense & Balance Tracker with File Export

def generate_ledger_summary(client_name, initial_balance, transactions):
    current_balance = initial_balance
    summary_lines = [f"--- Ledger Summary for {client_name} ---"]
    summary_lines.append(f"Starting Balance: KES {initial_balance:,.2f}\n")
    
    summary_lines.append("Transactions:")
    for desc, amount in transactions:
        current_balance += amount
        type_str = "Payment Received" if amount < 0 else "Charge Added"
        summary_lines.append(f" - {desc}: KES {abs(amount):,.2f} ({type_str})")
        
    summary_lines.append(f"\nFinal Outstanding Balance: KES {current_balance:,.2f}")
    
    whatsapp_msg = (
        f"\n*Payment Reminder for {client_name}*\n"
        f"Hello! Your current ledger balance is *KES {current_balance:,.2f}*.\n"
        f"Please review your statement and let us know if you have any questions."
    )
    
    return "\n".join(summary_lines), whatsapp_msg


def save_to_history(report_text):
    # Appends the generated report directly to a text file
    with open("ledger_history.txt", "a") as file:
        file.write(report_text + "\n" + "="*40 + "\n\n")


if __name__ == "__main__":
    client = "Acme Media"
    starting_amt = 15000.00
    
    tx_history = [
        ("Script Writing Service", 5000.00),
        ("Advance Payment", -10000.00),
        ("Video Editing Add-on", 3500.00)
    ]
    
    report, reminder = generate_ledger_summary(client, starting_amt, tx_history)
    
    # Print to console
    print(report)
    print("\n" + "="*40)
    print("WhatsApp Card Preview:")
    print("="*40)
    print(reminder)
    
    # Save automatically to file
    save_to_history(report)
    print("\n✓ Ledger summary successfully saved to ledger_history.txt")
