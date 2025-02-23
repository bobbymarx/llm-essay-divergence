import pandas as pd
from typing import List

def load_test_data(path: str) -> pd.DataFrame:
    """Load and validate test data"""
    df = pd.DataFrame(pd.read_csv(path))
    required_columns = ['id', 'topic']
    assert all(col in df.columns for col in required_columns), "Missing required columns"
    return df

def save_submission(df: pd.DataFrame, path: str) -> None:
    """Save submission file in the correct format"""
    required_columns = ['id', 'essay']
    assert all(col in df.columns for col in required_columns), "Missing required columns"
    df.to_csv(path, index=False) 