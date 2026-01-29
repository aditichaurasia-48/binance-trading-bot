import argparse
import logging

from bot.client import get_binance_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)
    validate_price(args.type, args.price)

    client = get_binance_client()

    order = place_order(
        client=client,
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("✅ ORDER PLACED")
    print(order)


if __name__ == "__main__":
    main()
