import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Log Analytics Dashboard", layout="wide")
st.title("Real-Time Log Monitoring & Anomaly Detection")

# Function to load the processed logs
def load_data():
    try:
        df = pd.read_csv("realtime_logs.csv")
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except FileNotFoundError:
        return pd.DataFrame()

# Layout
placeholder = st.empty()

while True:
    df = load_data()
    
    with placeholder.container():
        if not df.empty:
            # Stats Overview
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Logs", len(df))
            col2.metric("Errors Detected", len(df[df['level'] == 'ERROR']))
            col3.metric("Latest Service", df['service'].iloc[-1])

            # Error Frequency Chart
            st.subheader("Error Spikes Over Time")
            error_df = df[df['level'] == 'ERROR'].set_index('timestamp').resample('1min').size()
            st.line_chart(error_df)

            # Raw Data Table
            st.subheader("Recent Logs")
            st.dataframe(df.tail(10), use_container_width=True)
        else:
            st.warning("Waiting for data... Ensure main.py is running.")
            
    time.sleep(2) # Refresh every 2 seconds