# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

print("===================================")
print("     STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, "=", "$", price)

# Number of stocks
number_of_stocks = int(input("\nHow many different stocks do you want to buy? "))

# Take stock details
for i in range(number_of_stocks):

    stock_name = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Investment in", stock_name, "=", "$", investment)

    else:
        print("Stock not available!")

# Display total
print("\n===================================")
print("Total Investment = $", total_investment)
print("===================================")