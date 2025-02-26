import pandas as pd

def fetch_real_time_data():
    # Placeholder for real-time data fetching logic
    # Example: Fetching data from a REST API
    return pd.DataFrame({
        'temperature': [1500, 1550, 1520],
        'pressure': [60, 62, 61],
        'oxygen_level': [21, 22, 21.5]
    })

def load_historical_data(file_path):
    return pd.read_csv(file_path)
