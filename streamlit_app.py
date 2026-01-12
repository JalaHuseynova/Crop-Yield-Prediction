import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. AYARLAR VƏ FAYL YOLLARI ---
st.set_page_config(page_title="Crop Yield Analysis", layout="wide")

csv_name = "Crop_yield_with_weather_.csv"
model_name = "model.pkl"

# Fayl yollarını tapmaq
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, csv_name)
model_path = os.path.join(current_dir, model_name)

# --- 2. MƏLUMAT VƏ MODELİN YÜKLƏNMƏSİ ---
@st.cache_data
def load_data(path):
    if os.path.exists(path):
        data = pd.read_csv(path)
        data.columns = data.columns.str.strip()
        return data
    return None

@st.cache_resource
def load_model(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return pickle.load(f)
    return None

df = load_data(csv_path)
model = load_model(model_path)

# --- 3. SIDEBAR (NAVİQASİYA VƏ FİLTRLƏR) ---
st.sidebar.title("🔎 Navigation")
page = st.sidebar.radio("Go to:", ["Project Overview", "Data Exploration", "Yield Prediction"])

filtered_df = df

if df is not None:
    if 'Area' in df.columns:
        st.sidebar.divider()
        st.sidebar.header("🌐 Global Filters")
        all_countries = sorted(df['Area'].unique().tolist())
        selected_countries = st.sidebar.multiselect(
            "🌍 Select Countries:",
            options=all_countries,
            default=all_countries[:3] if len(all_countries) > 0 else []
        )
        min_year, max_year = int(df['Year'].min()), int(df['Year'].max())
        year_range = st.sidebar.slider("🗓️ Select Year Range:", min_year, max_year, (min_year, max_year))
        
        filtered_df = df[
            (df['Area'].isin(selected_countries)) &
            (df['Year'] >= year_range[0]) &
            (df['Year'] <= year_range[1])
        ]

# --- 4. SƏHİFƏLƏR ---
if page == "Project Overview":
    st.title("🌾 Crop Yield Prediction & Climate Analysis")
    st.markdown("""
    ### 🎯 Project Mission
    This project bridges the gap between climate science and agriculture. By analyzing historical yield records alongside temperature and precipitation patterns, we identify key environmental drivers of food production.

    ### 🔑 Key Features:
    * **Data Collection**: Integration of historical yield records and weather data.
    * **Exploratory Analysis**: Correlation studies between climate fluctuations and productivity.
    * **Machine Learning**: Predictive forecasting using a **Random Forest Regressor**.
    """)
    if os.path.exists("data_diagram.svg"):
        st.image("data_diagram.svg", caption="System Architecture")

elif page == "Data Exploration":
    st.title("📊 Data Exploration")
    if df is not None:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.subheader("Yield Trends Over Time")
            if not filtered_df.empty:
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.lineplot(data=filtered_df, x='Year', y='hg/ha_yield', hue='Item', ax=ax)
                plt.xticks(rotation=45)
                st.pyplot(fig)
            else:
                st.warning("Please select at least one country to see the chart.")
        with col2:
            st.subheader("Raw Data Preview")
            st.dataframe(filtered_df.head(10))
    else:
        st.error(f"CSV file '{csv_name}' missing!")

elif page == "Yield Prediction":
    st.title("Prediction Sandbox")
    if df is None:
        st.error("Dataset missing.")
    elif model is None:
        st.error(f"Model file '{model_name}' missing!")
    else:
        with st.form("prediction_form"):
            c1, c2 = st.columns(2)
            with c1:
                in_country = st.selectbox("Country:", sorted(df['Area'].unique()))
                in_item = st.selectbox("Crop:", sorted(df['Item'].unique()))
                in_year = st.number_input("Year:", value=2026)
            with c2:
                in_temp = st.slider("Temperature (°C):", -10, 40, 20)
                in_rain = st.number_input("Rainfall (mm):", value=1000)
                in_pest = st.number_input("Pesticides (tonnes):", value=100)

            if st.form_submit_button("Predict"):
                input_df = pd.DataFrame(columns=model.feature_names_in_)
                input_df.loc[0] = 0
                input_df['Year'] = in_year
                input_df['pesticides_tonnes'] = in_pest
                input_df['avg_temp'] = in_temp
                input_df['total_precip'] = in_rain
                
                area_col, item_col = f"Area_{in_country}", f"Item_{in_item}"
                if area_col in input_df.columns: input_df[area_col] = 1
                if item_col in input_df.columns: input_df[item_col] = 1
                
                res = model.predict(input_df)[0]
                st.success(f"### Predicted Yield: {res:,.2f} hg/ha")