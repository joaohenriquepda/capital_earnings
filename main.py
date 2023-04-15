#!/us/bin/
from functions.functions import calculate_profit, balanced_average_price

if __name__ == "__main__":
    movement_actions = [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
                        {"operation": "sell", "unit-cost": 2.00, "quantity": 5000},
                        {"operation": "sell", "unit-cost": 20.00,
                         "quantity": 2000},
                        {"operation": "sell", "unit-cost": 20.00,
                         "quantity": 2000},
                        {"operation": "sell", "unit-cost": 25.00,
                         "quantity": 1000},
                        {"operation": "buy", "unit-cost": 20.00,
                         "quantity": 10000},
                        {"operation": "sell", "unit-cost": 15.00,
                         "quantity": 5000},
                        {"operation": "sell", "unit-cost": 30.00,
                         "quantity": 4350},
                        {"operation": "sell", "unit-cost": 30.00, "quantity": 650}]

    # profit = calculate_profit(input_data)
    balanced_average_price(movement_actions)
    # for action in movement_actions:
    #     balanced_average_price(action=action)
