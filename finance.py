import pandas as pd
from pathlib import Path


def parse_finance_csv(file_path: Path) -> pd.DataFrame:
    """Parse CSV file into DataFrame with standardized columns."""
    df = pd.read_csv(file_path)
    # Ensure required columns exist
    if not {'date', 'amount', 'category'}.issubset(df.columns):
        raise ValueError("CSV must contain 'date', 'amount', 'category' columns")
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    return df


def calculate_monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate monthly income and expenses."""
    # Add income/expense marker
    df['type'] = df['amount'].apply(lambda x: 'income' if x > 0 else 'expense')
    # Group by month and type
    monthly = df.groupby([pd.Grouper(key='date', freq='M'), 'type'])['amount'].sum().unstack()
    return monthly.fillna(0)


def get_category_spending(df: pd.DataFrame) -> pd.Series:
    """Get total spending per category."""
    expenses = df[df['amount'] < 0]
    return expenses.groupby('category')['amount'].sum().abs().sort_values(ascending=False)
