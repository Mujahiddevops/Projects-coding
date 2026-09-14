# Intermediary Business Deal Margin Calculator

buyer_offer = 150000   # What the buyer pays you
seller_price = 120000  # What you pay the seller/supplier
transport_cost = 5000  # Operational expenses

# Calculations
gross_profit = buyer_offer - seller_price
net_profit = gross_profit - transport_cost
margin_percentage = (net_profit / buyer_offer) * 100

print("--- DEAL SUMMARY ---")
print(f"Buyer Offer:    KES {buyer_offer:,}")
print(f"Seller Price:   KES {seller_price:,}")
print(f"Transport/Fees: KES {transport_cost:,}")
print(f"Net Profit:     KES {net_profit:,}")
print(f"Profit Margin:  {margin_percentage:.2f}%")
print("✓ Termux and Acode are synced successfully!")
# Intermediary Business Deal Margin Calculator

buyer_offer = 150000   # What the buyer pays you
seller_price = 120000  # What you pay the seller
transport_cost = 5000  # Operational expenses

# Calculations
gross_profit = buyer_offer - seller_price
net_profit = gross_profit - transport_cost
margin_percentage = (net_profit / buyer_offer) * 100

print("--- DEAL SUMMARY ---")
print(f"Buyer Offer:    KES {buyer_offer:,}")
print(f"Seller Price:   KES {seller_price:,}")
print(f"Transport/Fees: KES {transport_cost:,}")
print(f"Net Profit:     KES {net_profit:,}")
print(f"Profit Margin:  {margin_percentage:.2f}%")
print("✓ Termux and Acode are synced successfully!")
# Interactive Business Deal Margin Calculator

print("=== INTERMEDIARY DEAL CALCULATOR ===")
buyer_offer = float(input("Enter Buyer's Offer (KES): "))
seller_price = float(input("Enter Seller's Asking Price (KES): "))
transport_cost = float(input("Enter Transport/Operational Costs (KES): "))

# Calculations
gross_profit = buyer_offer - seller_price
net_profit = gross_profit - transport_cost
margin_percentage = (net_profit / buyer_offer) * 100 if buyer_offer > 0 else 0

print("\n--- DEAL SUMMARY ---")
print(f"Buyer Offer:    KES {buyer_offer:,.2f}")
print(f"Seller Price:   KES {seller_price:,.2f}")
print(f"Transport/Fees: KES {transport_cost:,.2f}")
print(f"Net Profit:     KES {net_profit:,.2f}")
print(f"Profit Margin:  {margin_percentage:.2f}%")
import csv

print("=== INTERMEDIARY DEAL CALCULATOR ===")
buyer_offer = float(input("Enter Buyer's Offer (KES): "))
seller_price = float(input("Enter Seller's Asking Price (KES): "))
transport_cost = float(input("Enter Transport/Operational Costs (KES): "))

# Calculations
gross_profit = buyer_offer - seller_price
net_profit = gross_profit - transport_cost
margin_percentage = (net_profit / buyer_offer) * 100 if buyer_offer > 0 else 0

print("==================== DEAL SUMMARY ====================")

print(f"Buyer Offer:    KES {buyer_offer:,.2f}")
print(f"Seller Price:   KES {seller_price:,.2f}")
print(f"Transport/Fees: KES {transport_cost:,.2f}")
print(f"Net Profit:     KES {net_profit:,.2f}")
print(f"Profit Margin:  {margin_percentage:.2f}%")

# Save deal to CSV file
with open('/sdcard/Projects coding/deals.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([buyer_offer, seller_price, transport_cost, net_profit, f"{margin_percentage:.2f}%"])

print("\n✓ Deal successfully saved to deals.csv!")

