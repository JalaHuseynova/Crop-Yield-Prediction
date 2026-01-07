# 🌾 Crop yield prediction with weather data

## 📌 Overview

An end-to-end data analytics and machine learning project that analyzes historical crop yield data across multiple countries and predicts future agricultural productivity based on weather conditions obtained from an external API.

The project explores how climate factors influence crop yield and presents insights through an interactive Streamlit dashboard.

## 🎯 Key goals

Analyze crop yield trends by country and year

Study the impact of weather variables on agricultural productivity

Predict future crop yield using machine learning

Build an interactive dashboard for insights and forecasting

## 🧰 Tech stack

SQL – Data storage

Python – Data processing & modeling

Pandas, NumPy – Data manipulation

Matplotlib, Seaborn – Visualization

Machine learning- Model Training

Streamlit – Interactive dashboard

GitHub – Version control & documentation

## 🔄 Project workflow

End-to-end pipeline from raw data to yield prediction and visualization.
## Proyektin İşləmə Ardıcıllığı (Workflow)

```mermaid
graph TD
    %% Məlumat Mənbələri
    A[(CSV Files)] --> C[SQL Server]
    B[Weather API] --> C

    %% Saxlama və Analiz
    C --> D[EDA: Pandas, Seaborn, Matplotlib]
    
    %% Model və Nəticə
    D --> E[Machine Learning Model]
    E --> F[Streamlit Dashboard]
    F --> G{GitHub Repository}

    %% Rəngləndirmə (Daha professional görünüş üçün)
    style C fill:#0078D4,stroke:#fff,color:#fff
    style F fill:#FF4B4B,stroke:#fff,color:#fff
    style G fill:#238636,stroke:#fff,color:#fff

![Crop Yield Project Workflow](data_diagram.jpeg)

### Data Collection & Storage

Crop Yield Data: Historical agricultural data is loaded from a local CSV file into an SQL database.

Weather Data: Annual temperature data is collected from an external API and stored in the same SQL database.

### SQL → Python Processing

Data is retrieved from SQL into Python for analysis.

Initial data preprocessing is performed:

Data cleaning (Standardizing units and names)

Type conversions (Ensuring years and yield values are numeric)

Handling missing values

Exploratory Data Analysis (EDA) is conducted to uncover production trends over the years.

Visualizations are created using Matplotlib and Seaborn to illustrate the correlation between weather patterns and crop productivity.

### Machine Learning
A regression model is built to forecast crop yields based on historical performance and weather variables.

The model helps explore how factors like drought or high temperatures impact food security.

### Streamlit Dashboard
All insights and predictions are presented in an interactive Streamlit dashboard.

Users can filter by country or crop type to see historical trends and future yield forecasts.

## 📊 Output

Country-level yield trends

Weather impact analysis

Future crop yield predictions under different climate scenarios

## Team Members

[Gülgün Salamzadə](https://github.com/GulgunSalamzada)

[Ağacamal Aslanov](https://github.com/aghajamalaslanov-tech)
