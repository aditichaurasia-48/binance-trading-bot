def place_order(client, symbol, side, order_type, quantity, price=None):
    print("----- DRY RUN MODE -----")
    print(f"Symbol   : {symbol}")
    print(f"Side     : {side}")
    print(f"Type     : {order_type}")
    print(f"Quantity : {quantity}")
    if price:
        print(f"Price    : {price}")

    return {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "price": price,
        "status": "SIMULATED_SUCCESS"
    }
