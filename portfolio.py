STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 180,
    "MSFT": 420
}


def portfolio_tracker():
    total_investment = 0

    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))

    while True:
        stock = input("\nEnter stock name (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not available. Please choose from the available stocks.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            price = STOCK_PRICES[stock]
            investment = price * quantity
            total_investment += investment

            print("Price:", price)
            print("Quantity:", quantity)
            print("Investment:", investment)
        except ValueError:
            print("Please enter a valid number for quantity.")

    print("\nTotal Investment:", total_investment)


if __name__ == "__main__":
    portfolio_tracker()
