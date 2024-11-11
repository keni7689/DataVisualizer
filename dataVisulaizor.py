import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from io import BytesIO

# Set the page config
st.set_page_config(page_title='Advanced Data Visualizer',
                   layout='centered',
                   page_icon='📊')

# Title
st.title('📊 Advanced Data Visualizer')

# File uploader for CSV files
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    @st.cache_data
    def load_data(uploaded_file):
        return pd.read_csv(uploaded_file)

    df = load_data(uploaded_file)

    # Display a preview of the dataset
    st.write("### Preview of Dataset")
    st.dataframe(df.head())

    # Display basic statistics
    if st.checkbox('Show Data Summary'):
        st.write("### Data Summary")
        st.write(df.describe())

    # Show missing values
    if st.checkbox('Show Missing Values'):
        st.write("### Missing Values")
        st.write(df.isnull().sum())

    # Feature: Correlation Matrix
    if st.checkbox('Show Correlation Matrix'):
        st.write("### Correlation Matrix")
        corr = df.corr()
        fig_corr, ax_corr = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax_corr)
        st.pyplot(fig_corr)

    # Feature: Data Filtering
    st.write("### Data Filtering")
    filter_col = st.selectbox('Select a column to filter', options=df.columns)
    unique_values = df[filter_col].unique()
    selected_value = st.selectbox(f'Select value for {filter_col}', options=unique_values)
    filtered_df = df[df[filter_col] == selected_value]
    st.write("### Filtered Dataset")
    st.dataframe(filtered_df.head())

    # Allow the user to select columns for plotting
    columns = df.columns.tolist()

    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox('Select the X-axis', options=["None"] + columns)
    with col2:
        y_axis = st.selectbox('Select the Y-axis', options=["None"] + columns)

    plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot',
                 'Box Plot', 'Heatmap', 'Pie Chart']
    plot_type = st.selectbox('Select the type of plot', options=plot_list)

    if x_axis == "None" or (y_axis == "None" and plot_type != 'Pie Chart'):
        st.warning("Please select valid columns for both X and Y axes.")
    else:
        if st.button('Generate Plot'):
            fig, ax = plt.subplots(figsize=(8, 6))

            # Plot Types
            if plot_type == 'Line Plot':
                sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type == 'Bar Chart':
                sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type == 'Scatter Plot':
                sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type == 'Distribution Plot':
                sns.histplot(df[x_axis], kde=True, ax=ax)
            elif plot_type == 'Count Plot':
                sns.countplot(x=df[x_axis], ax=ax)
            elif plot_type == 'Box Plot':
                sns.boxplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type == 'Heatmap':
                sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
            elif plot_type == 'Pie Chart':
                df[x_axis].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
                ax.set_ylabel('')

            # Customization Options
            if st.checkbox('Customize Plot'):
                # Customize plot labels
                xlabel = st.text_input('X-axis label', value=x_axis)
                ylabel = st.text_input('Y-axis label', value=y_axis if y_axis != 'None' else '')
                title = st.text_input('Plot Title', value=f'{plot_type} of {y_axis} vs {x_axis}')
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.title(title)

            # Show the plot
            st.pyplot(fig)

            # Save Plot Option
            if st.checkbox('Save Plot as PNG'):
                buf = BytesIO()
                plt.savefig(buf, format="png")
                st.download_button(
                    label="Download Plot as PNG",
                    data=buf.getvalue(),
                    file_name="plot.png",
                    mime="image/png"
                )

else:
    st.info("Please upload a CSV file to proceed.")
