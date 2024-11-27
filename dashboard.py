import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

bike_df = pd.read_csv("bike_data.csv")
# Fungsi untuk membuat scatter plot
def plot_scatter(x, y1, y2, title1, title2, xlabel, ylabel1, ylabel2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    ax1.scatter(x, y1, color='blue', alpha=0.7)
    ax1.set_title(title1)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel1)
    ax2.scatter(x, y2, color='orange', alpha=0.7)
    ax2.set_title(title2)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel2)
    return fig

st.title("Rental Bike Dashboard")

# Pie Chart langsung ditampilkan tanpa tombol
total_registered_users = bike_df['registered'].sum()
total_casual_users = bike_df['casual'].sum()
categories = ['Registered', 'Casual']
values = [total_registered_users, total_casual_users]

fig, ax = plt.subplots()
ax.pie(
    values,
    labels=categories,
    autopct='%1.1f%%',
    startangle=90,
    colors=['skyblue', 'orange']
)
ax.set_title("User Distribution")
st.pyplot(fig)

# Scatter Plot: Temperature vs Users
if st.button("More Temperature More Users"):
    fig = plot_scatter(
        x=bike_df["temp"],
        y1=bike_df["casual"],
        y2=bike_df["registered"],
        title1="Casual Users vs Temperature",
        title2="Registered Users vs Temperature",
        xlabel="Temperature",
        ylabel1="Casual Users",
        ylabel2="Registered Users"
    )
    st.pyplot(fig)

# Scatter Plot: Humidity vs Users
if st.button("More Humidity Less Users"):
    fig = plot_scatter(
        x=bike_df["hum"],
        y1=bike_df["casual"],
        y2=bike_df["registered"],
        title1="Casual Users vs Humidity",
        title2="Registered Users vs Humidity",
        xlabel="Humidity",
        ylabel1="Casual Users",
        ylabel2="Registered Users"
    )
    st.pyplot(fig)
