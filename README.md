# DSA210-Project
## Overview
In this project, the relationship between immigration numbers and the economic performance of countries will be explored. Specifically, the goal is to understand how migration correlates with economic indicators such as GDP, GDP per capita, unemployment rate, and inflation. This analysis seeks to reveal information about the influence of immigration on the country's economy.

## Motivation
The economic impact of migration is highly controversial and significant for policymaking.This study intends to shed light on the ongoing debate on immigration laws and their effects on the economy. For this purpose, the data-driven relationships between migration and economic performance indicators will be analyzed.

## Data Sources
- **Immigration Data:**
    - **Source: World Bank and Kaggle**
      
- **Economic indicators:**
    - **Source:** World Bank
    - **Indicators**
      - GDP
      - GDP per capita
      - Inflation rate
      - Unemployment rate
     
- **Data Collection**
    - Migration data will be collected using the World Bank API via Python's wbdata library.
    - Additional supporting datasets from Kaggle will be downloaded as Excel or CSV files and imported into Python using pandas.
    - Data from both sources will be merged on common identifiers (country ISO codes and years) to prepare a cohesive dataset for analysis.

## Data Analysis
  - **Data Cleaning:** Handle missing data, detect and manage outliers, standardize variables.
  - **Exploratory Data Analysis (EDA):** To observe data distributions and initial relationships, visualizations will be generated.
  - **Correlation Analysis:** Pearson and Spearman correlations will be calculated for an evaluation of the tendency and degree of connection between immigration and economic indicators.

