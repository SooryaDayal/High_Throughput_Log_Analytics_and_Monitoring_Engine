import dask.dataframe as dd
import os

def load_structured_logs(file_path):
    """Loads structured CSV logs into a Dask DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file not found at: {file_path}")
    
    # Dask read_csv automatically handles headers and types
    df = dd.read_csv(file_path)
    
    # Ensure the timestamp is converted for time-series analysis
    df['timestamp'] = dd.to_datetime(df['timestamp'])
    
    return df