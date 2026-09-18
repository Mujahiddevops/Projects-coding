import unittest
from calculator import calculate_deal

class TestCalculator(unittest.TestCase):
    def test_margin_calculation(self):
        net_profit, margin = calculate_deal(100, 70, 10)
        self.assertEqual(net_profit, 20)
        self.assertEqual(margin, 20.0)

if __name__ == '__main__':
    unittest.main()


