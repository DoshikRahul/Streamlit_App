import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📅 7-Day Weather Forecast Simulator")

city = st.text_input("Enter your city:")

if st.button("Show Forecast"):
    if city.strip() == "":
        st.warning("Please enter a city name!")
    else:
        days = pd.date_range(start=pd.Timestamp.today(), periods=7).strftime("%a %d %b")
        temps = np.random.randint(10, 35, size=7)
        humidity = np.random.randint(40, 90, size=7)

        df = pd.DataFrame({
            "Day": days,
            "Temperature (°C)": temps,
            "Humidity (%)": humidity
        })

        st.write(f"7-day forecast for **{city.title()}**")
        st.dataframe(df)

        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()

        ax1.plot(days, temps, 'r-', marker='o', label='Temp (°C)')
        ax2.plot(days, humidity, 'b--', marker='x', label='Humidity (%)')

        ax1.set_xlabel("Day")
        ax1.set_ylabel("Temperature (°C)", color='r')
        ax2.set_ylabel("Humidity (%)", color='b')
        ax1.tick_params(axis='y', colors='r')
        ax2.tick_params(axis='y', colors='b')
        plt.title(f"7-Day Weather Forecast for {city.title()}")
        fig.autofmt_xdate()

        st.pyplot(fig)
