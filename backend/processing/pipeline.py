from backend.ingestion.loader import load_structured_logs

def build_pipeline(file_path):
    """Coordinates data loading and pre-processing for anomaly detection."""
    
    # 1. Load the data
    df = load_structured_logs(file_path)
    
    # 2. Sort by timestamp (Required for resample/divisions)
    df = df.sort_values('timestamp')
    
    # 3. Set index to timestamp to enable time-series operations
    # We use 'calculate_divisions=True' to help Dask know data boundaries
    df = df.set_index('timestamp', sorted=True)
    
    return df
