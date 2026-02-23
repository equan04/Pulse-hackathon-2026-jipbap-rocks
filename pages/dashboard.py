import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Recycling Dashboard")

st.title("My Recycling Impact Dashboard")

# stats
total_items = st.session_state.get("total_items", 42)
recycled_items = st.session_state.get("recycled_items", 31)
co2_saved = st.session_state.get("co2_saved", 8.4)
energy_saved = st.session_state.get("energy_saved", 52.0)

recycling_rate = (recycled_items / total_items) * 100


# top metrics
col1, col2, col3 = st.columns(3)

col1.metric("Items Scanned", total_items)
col2.metric("Recycling Rate", f"{recycling_rate:.1f}%")
col3.metric("Items Recycled", recycled_items)

st.divider()

# Environmental impact section
st.subheader("Environmental Impact")

col4, col5 = st.columns(2)

col4.metric("CO₂ Saved", f"{co2_saved:.2f} kg")
col5.metric("Energy Saved", f"{energy_saved:.1f} kWh")

st.caption("Estimates based on average recycling impact data.")

st.divider()


# show recycling progress over time 
st.subheader("Recycling Progress Over Time")

days = 30
dates = pd.date_range(end=pd.Timestamp.today(), periods=days)

trend = np.linspace(5, recycled_items, days) + np.random.normal(0, 1, days)
trend = np.clip(trend, 0, None)

df = pd.DataFrame({
    "Date": dates,
    "Recycled Items": trend
}).set_index("Date")

st.line_chart(df)

st.divider()



# impact equivalents
st.subheader("What That Means")

trees_saved = co2_saved / 21  # ~21 kg CO2 absorbed per tree/year
phone_charges = energy_saved * 8  # ~1 kWh = ~8 phone charges

st.write(f"Equivalent to **{trees_saved:.2f} trees** absorbing CO₂ for a year.")
st.write(f"Enough energy to charge a smartphone **{int(phone_charges)} times**.")

st.divider()

if st.button("Back to Classifier"):
    st.switch_page("app.py")