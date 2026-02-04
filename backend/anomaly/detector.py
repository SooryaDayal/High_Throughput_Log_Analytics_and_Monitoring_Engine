import pandas as pd
import numpy as np

def detect_anomaly(df, z_threshold=2):
    """
    Analyzes log data to detect statistical spikes in error counts.
    Uses Z-Score: (x - mean) / std_dev
    """
    # 1. Resample to 1-minute intervals and count errors
    # We use .compute() because statistical analysis is easier on a smaller Pandas series
    error_series = df[df["level"] == "ERROR"].resample("1min").size().compute()

    if error_series.empty or error_series.sum() == 0:
        return pd.DataFrame()

    # 2. Calculate Statistics
    mean_val = error_series.mean()
    std_val = error_series.std()

    # Handle cases with zero variance (no variation in error counts)
    if std_val == 0 or np.isnan(std_val):
        return pd.DataFrame()

    # 3. Calculate Z-Scores
    z_scores = (error_series - mean_val) / std_val

    # 4. Identify Anomalies
    anomalies = error_series[z_scores > z_threshold].reset_index()
    anomalies.columns = ["timestamp", "error_count"]
    
    # Add the Z-Score to the results for the email alert
    anomalies["z_score"] = z_scores[z_scores > z_threshold].values

    return anomalies