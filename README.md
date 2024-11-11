# Advanced Data Visualizer 📊

An interactive data visualization tool built with Streamlit that enables users to upload CSV files and gain insights through a variety of customizable plots and data summaries. This tool is designed for real-time data analysis, offering functionalities to explore correlations, visualize distributions, and generate reports with ease.

## Features

- **CSV Upload**: Upload any CSV file for instant data visualization.
- **Data Summary**: View statistical summaries and detect missing values.
- **Correlation Matrix**: Display and analyze correlations using a heatmap.
- **Data Filtering**: Filter data by specific columns and values.
- **Customizable Plots**: Generate various plots (Line, Bar, Scatter, Distribution, Count, Box, Heatmap, Pie) with options for custom labels and titles.
- **Downloadable Plots**: Save generated plots as PNG images.

## Tools and Libraries

- **Streamlit**: For creating the interactive web app interface.
- **Pandas**: For data manipulation and processing.
- **Matplotlib & Seaborn**: For plotting and data visualization.
- **Plotly**: For interactive and detailed visualizations.

## How to Run the Project

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/advanced-data-visualizer.git
    cd advanced-data-visualizer
    ```

2. **Install Dependencies**
    Make sure you have Python installed, then install required packages:
    ```bash
    pip install streamlit pandas matplotlib seaborn plotly
    ```

3. **Run the Application**
    ```bash
    streamlit run app.py
    ```

4. **Upload a CSV File**: Once the app is running, upload a CSV file to begin data visualization.

## Usage Instructions

- **Data Summary**: Check the "Show Data Summary" checkbox to view statistical information.
- **Missing Values**: Check the "Show Missing Values" checkbox to identify missing data.
- **Correlation Matrix**: Enable this to display a heatmap of data correlations.
- **Generate Plots**: Select X and Y axes, choose a plot type, and customize labels if needed.
- **Download Plot**: Save your plot as a PNG by selecting the "Save Plot as PNG" checkbox.

## Screenshots

(Add screenshots of the app's UI here, if available.)

## License

This project is licensed under the MIT License.
