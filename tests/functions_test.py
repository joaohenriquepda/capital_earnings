import unittest
from functions.functions import calculate_profit, balanced_average_price


class TestCalculateProfit(unittest.TestCase):
    def test_case1(self):
        movement_actions = [{"operation": "buy", "unit-cost": 10.00, "quantity": 100},
                            {"operation": "sell", "unit-cost": 15.00, "quantity": 50},
                            {"operation": "sell", "unit-cost": 15.00, "quantity": 50}]

        result = balanced_average_price(movement_actions)
        expected_return = [{"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}]
        self.assertEqual(result, expected_return)

    def test_case2(self):
        movement_actions = [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
                            {"operation": "sell", "unit-cost": 20.00,
                                "quantity": 5000},
                            {"operation": "sell", "unit-cost": 5.00, "quantity": 5000}]

        result = balanced_average_price(movement_actions)
        expected_return = [{"tax": 0.00}, {"tax": 10000.00}, {"tax": 0.00}]
        self.assertEqual(result, expected_return)

    def test_case3(self):
        movement_actions = [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
                            {"operation": "sell", "unit-cost": 5.00, "quantity": 5000},
                            {"operation": "sell", "unit-cost": 20.00, "quantity": 3000}]

        result = balanced_average_price(movement_actions)
        expected_return = [{"tax": 0.00}, {"tax": 0.00}, {"tax": 1000.00}]
        self.assertEqual(result, expected_return)

    def test_case4(self):
        movement_actions = [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
                            {"operation": "buy", "unit-cost": 25.00, "quantity": 5000},
                            {"operation": "sell", "unit-cost": 15.00, "quantity": 10000}]

        result = balanced_average_price(movement_actions)
        expected_return = [{"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}]
        self.assertEqual(result, expected_return)

    def test_case5(self):
        movement_actions = [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
                            {"operation": "buy", "unit-cost": 25.00, "quantity": 5000},
                            {"operation": "sell", "unit-cost": 15.00,
                                "quantity": 10000},
                            {"operation": "sell", "unit-cost": 25.00, "quantity": 5000}]

        result = balanced_average_price(movement_actions)
        expected_return = [{"tax": 0.00}, {"tax": 0.00},
                           {"tax": 0.00}, {"tax": 10000.00}]
        self.assertEqual(result, expected_return)

    def test_case6(self):
        movement_actions = [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
                            {"operation": "sell", "unit-cost": 2.00, "quantity": 5000},
                            {"operation": "sell", "unit-cost": 20.00,
                                "quantity": 2000},
                            {"operation": "sell", "unit-cost": 20.00,
                                "quantity": 2000},
                            {"operation": "sell", "unit-cost": 25.00, "quantity": 1000}]

        result = balanced_average_price(movement_actions)
        expected_return = [{"tax": 0.00}, {"tax": 0.00}, {
            "tax": 0.00}, {"tax": 0.00}, {"tax": 3000.00}]
        self.assertEqual(result, expected_return)

    def test_case7(self):
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

        result = balanced_average_price(movement_actions)
        expected_return = [{"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}, {"tax": 0.00}, {"tax": 3000.00},
                           {"tax": 0.00}, {"tax": 0.00}, {"tax": 3700.00}, {"tax": 0.00}]
        self.assertEqual(result, expected_return)

    def test_case8(self):
        movement_actions = [{"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
                            {"operation": "sell", "unit-cost": 50.00,
                                "quantity": 10000},
                            {"operation": "buy", "unit-cost": 20.00,
                                "quantity": 10000},
                            {"operation": "sell", "unit-cost": 50.00, "quantity": 10000}]

        result = balanced_average_price(movement_actions)
        expected_return = [{"tax": 0.00}, {"tax": 80000.00}, {
            "tax": 0.00}, {"tax": 60000.00}]
        self.assertEqual(result, expected_return)
