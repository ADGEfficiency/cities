import pandas as pd
import streamlit as st

data = pd.DataFrame(
    {
        "city": ["auckland", "berlin", "london"],
        "population": [1.6, 3.6, 8.9],
        "hemisphere": ["south", "north", "north"],
    }
)

st.header("Cities Dataset")
st.text(f"shape: {data.shape}")
st.dataframe(data)

#  selectbox to view data for one city
cities = data["city"].tolist()
selected_city = st.selectbox("Select a city:", cities)
city = data.loc[data["city"] == selected_city]
assert city.shape[0] == 1
st.write(city)
st.write(f"selected: {selected_city}\n")
st.write(f"population: {float(city['population'].iloc[0])}")
st.write(f"hemisphere: {city['hemisphere'].values[0]}")

#  bar chart of population
st.bar_chart(data, y="population")
