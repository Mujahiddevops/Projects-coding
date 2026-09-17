# Unit tests for calculator functions

def calculate_margin(buyer_offer, seller_price, transport_cost):
    gross_profit = buyer_offer - seller_price
    net_profit = gross_profit - transport_cost
    margin_percentage = (net_profit / buyer_offer) * 100
    return net_profit, margin_percentage

def test_profit_calculation():
    net_profit, margin = calculate_margin(150000, 120000, 5000)
    assert net_profit == 25000
    assert round(margin, 2) == 16.67

def test_break_even():
    net_profit, margin = calculate_margin(100000, 90000, 10000)
    assert net_profit == 0
    assert margin == 0.0
