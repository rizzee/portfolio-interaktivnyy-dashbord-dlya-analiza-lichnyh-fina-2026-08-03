import unittest
from pathlib import Path
import pandas as pd
from finance import parse_finance_csv


class TestFinance(unittest.TestCase):
    def setUp(self):
        self.test_csv = "date,amount,category\n2023-01-01,100,Groceries\n2023-01-02,200,Transport"
        self.test_file = Path('test.csv')
        self.test_file.write_text(self.test_csv)

    def tearDown(self):
        if self.test_file.exists():
            self.test_file.unlink()

    def test_parse_finance_csv(self):
        df = parse_finance_csv(self.test_file)
        self.assertEqual(len(df), 2)
        self.assertListEqual(df.columns.tolist(), ['date', 'amount', 'category'])

    def test_parse_finance_csv_missing_columns(self):
        invalid_csv = "date,amount\n2023-01-01,100"
        invalid_file = Path('invalid.csv')
        invalid_file.write_text(invalid_csv)

        with self.assertRaises(ValueError):
            parse_finance_csv(invalid_file)
        
        if invalid_file.exists():
            invalid_file.unlink()


if __name__ == '__main__':
    unittest.main()
