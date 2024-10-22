import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

# Initialize the Streamlit app with a title
st.title("Efficient Data Stream Anomaly Detection")

# Sidebar for user-defined parameters
# Slider for selecting the window size for anomaly detection
window_size = st.sidebar.slider("Window Size", min_value=10, max_value=100, value=50, step=10)
# Slider for selecting the Z-score threshold for detecting anomalies
threshold = st.sidebar.slider("Anomaly Detection Threshold (Z-score)", min_value=1.0, max_value=5.0, value=2.5, step=0.1)

# Function to simulate a data stream with seasonal patterns, noise, and anomalies
def simulate_data_stream(num_points=500):
    # Generate seasonal pattern using sine function
    data = np.sin(np.linspace(0, 50, num_points))  
    # Add Gaussian noise to the data
    noise = np.random.normal(0, 0.2, num_points)  
    # Introduce random anomalies with a 5% probability
    anomalies = np.random.choice([0, 1], size=num_points, p=[0.95, 0.05])  
    # Combine noise and anomalies into the data
    data += noise + anomalies * np.random.normal(5, 1, num_points)  
    return data

# Function for detecting anomalies using a rolling window Z-score method
def detect_anomalies(data, window_size, threshold):
    # Calculate rolling mean and standard deviation
    rolling_mean = pd.Series(data).rolling(window=window_size).mean()
    rolling_std = pd.Series(data).rolling(window=window_size).std()
    
    # Calculate Z-scores
    z_scores = (data - rolling_mean) / rolling_std
    
    # Identify anomalies based on the Z-score threshold
    anomalies = np.where(np.abs(z_scores) > threshold, True, False)
    return anomalies

# Initialize a deque to hold the data stream, limiting its size to the window size
data_stream = deque(maxlen=window_size)

# Function for plotting the data and detected anomalies
def plot_data(data, anomalies):
    # Create a plot with a specified size
    fig, ax = plt.subplots(figsize=(12, 6))
    # Plot the data stream
    ax.plot(data, label="Data Stream", color="blue")
    # Highlight anomalies in red
    ax.scatter(np.arange(len(data))[anomalies], np.array(data)[anomalies], color="red", label="Anomalies")
    ax.legend()  # Show legend
    
    # Create three equal columns to display the plot
    cols = st.columns(3)
    # Plot the figure in each column
    for col in cols:
        with col:
            st.pyplot(fig)

# Function to run the real-time detection simulation
def run_real_time_detection():
    # Simulate a data stream
    data = simulate_data_stream()
    for i in range(len(data)):
        # Append the current data point to the stream
        data_stream.append(data[i])
        
        # Check if the data stream is at least the size of the window
        if len(data_stream) == window_size:
            # Detect anomalies in the current data stream
            anomalies = detect_anomalies(np.array(data_stream), window_size, threshold)
            # Plot the data and detected anomalies
            plot_data(data_stream, anomalies)
        
        # Stop the loop if the running state is set to False
        if not st.session_state.running:
            break

# Initialize session state for running if not already present
if 'running' not in st.session_state:
    st.session_state.running = False

# Control button to start or stop the detection
if st.button("Start/Stop Real-Time Detection"):
    # Toggle the running state
    st.session_state.running = not st.session_state.running  
    if st.session_state.running:
        st.session_state.data_counter = 0  # Reset counter on start
        # Continuously run detection while in running state
        while st.session_state.running:
            run_real_time_detection()
    else:
        # Notify that real-time detection has stopped
        st.write("Real-Time Detection Stopped.")
