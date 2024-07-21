def print_transactions(cash, num_stocks, num_days, stock_names, stocks_owned, stock_prices):
    transactions = []
    moving_average_period = 5  # Use a 5-day moving average period for more reliability
    
    for i in range(num_stocks):
        stock_name = stock_names[i]
        shares_owned = stocks_owned[i]
        prices = stock_prices[i]
        num_prices = len(prices)
        latest_price = prices[-1]

        if num_prices < moving_average_period:
            continue  # Skip stocks without enough price history
        
        # Calculate the moving average
        moving_average = sum(prices[-moving_average_period:]) / moving_average_period
        
        # Calculate the price difference from the moving average
        price_difference = moving_average - latest_price
        
        if price_difference > 1.5 and cash >= latest_price:
            shares_to_buy = int(cash // latest_price)
            if shares_to_buy > 0:
                transactions.append(f"{stock_name} BUY {shares_to_buy}")
                cash -= shares_to_buy * latest_price
        elif price_difference < -1.5 and shares_owned > 0:
            transactions.append(f"{stock_name} SELL {shares_owned}")
    
    if transactions:
        print(len(transactions))
        for transaction in transactions:
            print(transaction)
    else:
        print(0)

def input_parameters():
    cash, num_stocks, num_days = map(float, input().split())
    num_stocks = int(num_stocks)
    num_days = int(num_days)
    stock_names = []
    stocks_owned = []
    stock_prices = []
    
    for _ in range(num_stocks):
        input_line = input().strip().split()
        stock_names.append(input_line[0])
        stocks_owned.append(int(input_line[1]))
        stock_prices.append(list(map(float, input_line[2:])))
        
    return cash, num_stocks, num_days, stock_names, stocks_owned, stock_prices

cash, num_stocks, num_days, stock_names, stocks_owned, stock_prices = input_parameters()

print_transactions(cash, num_stocks, num_days, stock_names, stocks_owned, stock_prices)

# Example Input:
# 90 2 400
# iStreet 10 4.54 5.53 6.56 5.54 7.60
# HR 0 30.54 27.53 24.42 20.11 17.50
