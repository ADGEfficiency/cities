import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_option("deprecation.showPyplotGlobalUse", False)

data = {
    "city": ["auckland", "berlin", "london"],
    "population": [1.6, 3.6, 8.9],
    "hemisphere": ["south", "north", "north"],
}

df = pd.DataFrame(data)

st.header("Cities Dataset")
st.text("Take a look at the cities dataset with Streamlit:")
st.dataframe(df)

cities = df["city"].tolist()
selected_city = st.selectbox("Select a city:", cities)
st.write("You selected ", selected_city)
st.write(
    "Population of the selected city is:",
    df.loc[df["city"] == selected_city]["population"].values,
)
st.write(
    "Hemisphere of the selected city is:",
    df.loc[df["city"] == selected_city]["hemisphere"].values,
)

st.write("Cities Population")
st.bar_chart(df["population"])

plt.bar(df["city"], df["population"])
st.pyplot()
