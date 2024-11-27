import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

bike_df = pd.read_csv("bike_data.csv")


# Fungsi Membuat Pie Chart untuk Distribusi User
def pie_distribution():
    total_casual = bike_df['casual'].sum()
    total_registered = bike_df['registered'].sum()
    labels = ['Casual User', 'Registered User']
    values = [total_casual, total_registered]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange'])
    ax.set_title('Distribusi Casual vs Registered User')
    return fig

def scatter_side_by_side():
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))  # 1 baris, 2 kolom

    # Scatter plot: Temperature vs Casual User
    axes[0].scatter(bike_df['temp'], bike_df['casual'], color='blue', label='Casual User')
    axes[0].set_title('Temperature vs Casual User')
    axes[0].set_xlabel('Temperature')
    axes[0].set_ylabel('Casual User')
    axes[0].legend()

    # Scatter plot: Temperature vs Registered User
    axes[1].scatter(bike_df['temp'], bike_df['registered'], color='green', label='Registered User')
    axes[1].set_title('Temperature vs Registered User')
    axes[1].set_xlabel('Temperature')
    axes[1].set_ylabel('Registered User')
    axes[1].legend()

    plt.tight_layout()  # Menyesuaikan tata letak
    return fig


# streamlit
st.title("Visualisasi Data Pengguna")
st.subheader("Pie Chart: Distribusi Casual vs Registered User")
st.pyplot(pie_distribution())


st.title("Scatter Plot Berdampingan")
st.pyplot(scatter_side_by_side())


