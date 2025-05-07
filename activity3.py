# -*- coding: utf-8 -*-
"""
Created on Sun May  4 15:32:14 2025
@author: Administrator
"""

import streamlit as st
import streamlit.components.v1 as components

# Apply page config
st.set_page_config(
    page_title="Data Warehousing & Enterprise Data Management",
    page_icon="🏢",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f9fcff;
        }
        .stSidebar {
            background-color: #e7f0fa;
        }
        .block-container {
            padding: 2rem 2rem 2rem 2rem;
        }
        .stTabs [role="tab"] {
            font-size: 16px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Filters
st.sidebar.title("🔍 Filters & Options")
topic = st.sidebar.selectbox(
    "Choose a Topic:",
    ["Data Warehousing", "ETL Processes", "Enterprise Data Management", "Data Governance"]
)
filter_value = st.sidebar.slider("🔧 Importance Level", 0, 100, 50)

# Main Title
st.title("🏢 Data Warehousing & Enterprise Data Management")
st.markdown(f"### You selected **{topic}** with an importance level of **{filter_value}**.")

# Layout with Columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📦 Data Warehousing Concepts")
    st.success("""
    - Centralized data storage system  
    - Optimized for query and analysis  
    - Supports decision-making with historical data  
    """)

with col2:
    st.markdown("#### ⚙️ ETL Process")
    st.info("""
    - **Extract** data from multiple sources  
    - **Transform** it into consistent format  
    - **Load** into data warehouse  
    """)

# Tabs for organized content
tab1, tab2 = st.tabs(["📚 Definitions", "📈 Use Cases"])

with tab1:
    st.markdown("### 📘 Key Definitions")
    st.warning("""
    - **Data Warehouse**: A system for reporting and data analysis  
    - **Data Governance**: Policies and procedures for managing data assets  
    - **Enterprise Data Management**: The practice of managing data as a strategic asset  
    """)

with tab2:
    st.markdown("### 💡 Real-world Use Cases")
    st.success("""
    - Business Intelligence dashboards  
    - Customer behavior analytics  
    - Compliance and auditing data stores  
    """)

# Expander for extra info
with st.expander("📖 More Information"):
    st.markdown("""
    Data Warehousing and Enterprise Data Management are essential for aligning IT capabilities with business needs.  
    Modern tools support real-time analytics, cloud storage, and AI integration for smarter insights.
    """)

# Optional: Add footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</div>",
    unsafe_allow_html=True
)
