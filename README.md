# DSA210 Project: The Relationship Between Immigration and Economic Performance

##  Overview
This project investigates the relationship between immigration trends and economic performance across selected countries from 1980 to 2024. The goal is to analyze how migration correlates with key indicators such as GDP, GDP per capita, unemployment rate, inflation, education and health expenditures, life expectancy, and income inequality (Gini index). This comprehensive analysis aims to provide data-driven insights into the socio-economic impacts of migration.

##  Research Questions
1. Does the percentage of migrants in a population significantly correlate with a country's GDP?
2. Is there a relationship between migrant density and GNI per capita (a measure of individual wealth)?
3. How does migration affect unemployment rates in different countries?
4. Is there a noticeable impact of migration on social indicators such as education expenditure, health spending, and life expectancy?
5. Does higher immigration contribute to increased or decreased income inequality, as measured by the Gini Index?

##  Motivation
The economic impact of migration is highly controversial and significant for policymaking.This study intends to shed light on the ongoing debate on immigration laws and their effects on the economy. For this purpose, the data-driven relationships between migration and economic performance indicators will be analyzed.

##  Data Sources
- **Primary Source:** World Bank
- **Additional Support:** Kaggle datasets (for interpolated or more recent migration data)

###  Indicators Collected
- **Migration Data:**
  - Net Migration
  - Migrant Stock (Total)
  - Migrant % of Population (calculated)

- **Economic & Social Indicators:**
  - GDP (Current US$)
  - GNI per Capita
  - Unemployment Rate
  - Inflation Rate
  - Total Population
  - Education Expenditure (% of GDP)
  - Health Expenditure (% of GDP)
  - Life Expectancy at Birth
  - Gini Index

The dataset has been enriched by adding some socioeconomic parameters as well as economic data.
##  Data Collection & Cleaning
- Raw data files stored in `/raw_data`
- Cleaned, selected data saved in `/data`
- Data range: 1980–2024 (where available)
- Country focus: USA, DEU, CAN, GBR, AUS, TUR, MEX, IND. These are developed and developing countries with the highest migration traffic.

### Steps Taken:
- Restructured datasets to long-format
- Filtered by country and year
- Handled missing values and standardization

##  Exploratory Data Analysis (EDA)
- Descriptive statistics for all indicators
- Time-series trends (e.g., migrant % of population over time)
- Heatmap visualization of indicator correlations
- Country-level comparisons

##  Hypotheses
###  Economic Hypothesis:
- **H₀ (Null Hypothesis):** Migrant % of Population has no significant effect on core economic indicators (GDP, GNI per capita, Unemployment Rate, Inflation).
- **H₁ (Alternative Hypothesis):** Migrant % of Population significantly affects core economic indicators.
###  Socioeconomic Hypothesis:
- **H₀ (Null Hypothesis):** Migrant % of Population has no significant effect on social indicators (Education Expenditure, Health Expenditure, Life Expectancy, Gini Index).
- **H₁ (Alternative Hypothesis):** Migrant % of Population significantly affects social indicators.

Significance levels and interpretation were reported for each.

##  Tools Used
- Python (Pandas, NumPy)
- Visualization: Matplotlib, Seaborn
- Statistical Analysis: SciPy (Pearson/Spearman)

## Findings
- A weak but statistically significant positive correlation was found between Migrant % of Population and GDP (H₀ rejected).
- A strong, highly significant positive correlation exists between Migrant % of Population and GNI per Capita (H₀ rejected).
- A moderate negative correlation was observed between Migrant % of Population and Inflation Rate (H₀ rejected).
- No statistically significant relationship was found between Migrant % of Population and Unemployment Rate (H₀ not rejected).
- Strong positive correlations were found between Migrant % of Population and both Health and Education Expenditures (H₀ rejected).
- A very strong positive correlation was observed between Migrant % of Population and Life Expectancy (H₀ rejected).
- A moderate negative correlation was found between Migrant % of Population and Gini Index (H₀ rejected), suggesting that higher migration may contribute slightly to lower income inequality.

## Machine Learning

### Objective
We aimed to predict the log-transformed GDP of selected countries using migration rates and a combination of economic and social indicators from 1980–2024.

### Features Used
- Migrant % of Population
- log(GNI per Capita)
- Unemployment Rate
- Inflation Rate
- Health Expenditure (% GDP)
- Education Expenditure (% GDP)
- Life Expectancy
- Gini Index

### Transformations
- Applied log transformation to GDP and GNI per Capita to handle scale differences.

### Models Applied
1. **Linear Regression**
   - R² score: 0.896
   - RMSE: 0.267

2. **Decision Tree Regressor**
   - R² score: 0.860
   - RMSE: 0.309

3. **Random Forest Regressor**
   - R² score: 0.824
   - RMSE: 0.347
### Results & Interpretation
Random Forest provided the strongest predictive power, outperforming both linear regression and a single decision tree. Feature importance analysis revealed that log(GNI per Capita), Health Expenditure, Gini Index, and Migrant % of Population were the most influential in predicting GDP.


![Feature Importance](images/feature_importance.png)
![Actual vs Predicted](images/actual_vs_predicted.png)

### Visualizations Included
- Actual vs Predicted plots for each model.
- Feature Importance (Random Forest).
- Residual Distribution plots for Random Forest and Decision Tree.

## Requirements

- Python 3.10+
- pandas==2.0.3
- numpy==1.24.3
- scikit-learn==1.2.2
- matplotlib==3.7.1
- seaborn==0.12.2
- scipy==1.10.1

  
## Limitations and Future Work

- Some datasets had missing or incomplete years, which may affect long-term trend analysis.
- The models are trained without hyperparameter tuning; further optimization could improve performance.
- Future work can include adding time series models, expanding the feature set (e.g., political stability, trade balance), or using ensemble methods like XGBoost.
- Causal analysis or policy impact simulations could provide even deeper insights.

