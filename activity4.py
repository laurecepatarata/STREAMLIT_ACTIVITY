import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="COVID-19 Dashboard",
    layout="wide",
    page_icon="🦠"
)

# Custom CSS for cleaner styling
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🌍 COVID-19 Statistics Dashboard")

# Sidebar - Country selection
st.sidebar.header("📌 Choose a Country")
countries_url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(countries_url)
country_data = response.json()
country_list = sorted([country['country'] for country in country_data])
selected_country = st.sidebar.selectbox("Select a Country", country_list)

# Fetch data
stats_url = f"https://disease.sh/v3/covid-19/historical/{selected_country}?lastdays=30"
latest_url = f"https://disease.sh/v3/covid-19/countries/{selected_country}"
historic_res = requests.get(stats_url).json()
latest_res = requests.get(latest_url).json()

# Main content
if "timeline" in historic_res:
    data = historic_res['timeline']
    df_cases = pd.DataFrame(data['cases'].items(), columns=['Date', 'Cases'])
    df_deaths = pd.DataFrame(data['deaths'].items(), columns=['Date', 'Deaths'])
    df_recovered = pd.DataFrame(data['recovered'].items(), columns=['Date', 'Recovered'])

    # Merge and clean
    df_all = pd.merge(df_cases, df_deaths, on='Date')
    df_all = pd.merge(df_all, df_recovered, on='Date')
    df_all['Date'] = pd.to_datetime(df_all['Date'])

    # Trends Line Chart
    st.subheader(f"📊 COVID-19 Trends in {selected_country} (Last 30 Days)")
    st.line_chart(df_all.set_index('Date'))

    # Latest Summary Bar Chart
    st.subheader(f"🧾 Latest Totals in {selected_country}")
    latest_df = pd.DataFrame({
        'Category': ['Cases', 'Deaths', 'Recovered'],
        'Count': [latest_res['cases'], latest_res['deaths'], latest_res['recovered']]
    })
    st.bar_chart(latest_df.set_index('Category'))

    # New Cases Area Chart
    st.subheader("📈 New Cases Trend")
    df_all['New Cases'] = df_all['Cases'].diff().fillna(0)
    st.area_chart(df_all.set_index('Date')['New Cases'])

    # Pie Chart using Matplotlib
    st.subheader("🧩 Case Distribution (Pie Chart)")
    fig, ax = plt.subplots()
    labels = ['Active', 'Recovered', 'Deaths']
    values = [latest_res['active'], latest_res['recovered'], latest_res['deaths']]
    colors = ['#FFDD57', '#28C76F', '#EA5455']
    ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')
    st.pyplot(fig)

    # Raw Data Table
    st.subheader("📋 Raw Data Table")
    st.dataframe(df_all)

else:
    st.error("🚫 Historical data not available for this country.")

# Optional: Footer
st.markdown("---")
st.markdown("<center><sub>Made with ❤️ using Streamlit and disease.sh API</sub></center>", unsafe_allow_html=True)
