Here's a **README.md** file that includes details about the web app, dependencies, usage instructions, and a breakdown of all the functions:

---

# Efficient Data Stream Anomaly Detection Web App

This web app, built using Streamlit, performs real-time anomaly detection on a simulated data stream of floating-point numbers. It is designed to identify unusual patterns, such as exceptionally high values or deviations from the norm, using a rolling window z-score method.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [How to Use](#how-to-use)
6. [Customization](#customization)

## Project Overview

The goal of this project is to detect anomalies in a continuous data stream, such as financial transactions or system metrics. The web app includes real-time visualization of the data stream and highlights detected anomalies. The anomaly detection algorithm uses a rolling window and z-score method, with configurable parameters.

## Features

- Real-time data stream simulation with random anomalies and seasonal patterns.
- Anomaly detection based on a rolling window z-score calculation.
- Real-time plotting of data streams and flagged anomalies.
- User-adjustable parameters for window size and z-score threshold.
- Simple and intuitive interface built using Streamlit.

## Technologies Used

- **Python 3.x**
- **Streamlit** for the web interface.
- **Numpy** for data stream generation.
- **Pandas** for rolling window calculations.
- **Matplotlib** for real-time data plotting.

## Installation

To install and run the app, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/raamlaa/data-stream-anomaly-detection.git
   cd data-stream-anomaly-detection
   ```

2. **Install dependencies** using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   The required libraries are:

   - `streamlit`
   - `numpy`
   - `pandas`
   - `matplotlib`

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## How to Use

1. Adjust the **Window Size** and **Z-Score Threshold** using the sidebar sliders.
2. Click **Start Real-Time Detection** to begin the anomaly detection process.
3. The plot will update in real-time, showing the data stream (in blue) and detected anomalies (highlighted in red).

## Customization

- **Algorithms**: You can switch to other anomaly detection algorithms such as Isolation Forest or more advanced time-series forecasting methods.
- **Data Stream**: Modify the `simulate_data_stream` function to better represent your real-world use case, such as by adding more sophisticated noise or seasonal effects.
