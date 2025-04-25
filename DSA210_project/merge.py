import pandas as pd

# Loading all cleaned datasets
gdp = pd.read_csv("data/gdp_selected_1980_2024.csv")
gni = pd.read_csv("data/gni_per_capita_selected_1980_2024.csv")
unemp = pd.read_csv("data/unemployment_selected_1995_2019.csv")
inflation = pd.read_csv("data/inflation_selected_1980_2024.csv")
migration = pd.read_csv("data/net_migration_selected_1980_2024.csv")
population = pd.read_csv("data/population_selected_1980_2024.csv")
migrant_stock = pd.read_csv("data/migrant_stock_selected_1980_2024.csv")
health_exp = pd.read_csv("data/health_expenditure_selected_1980_2024.csv")
education_exp = pd.read_csv("data/education_expenditure_selected_1980_2024.csv")
life_expectancy = pd.read_csv("data/life_expectancy_selected_1980_2024.csv")
gini_index = pd.read_csv("data/gini_index_selected_1980_2024.csv")

# Merge step by step on country, code, and year
merged = gdp.merge(gni, on=["Country Name", "Country Code", "Year"], how="outer")
merged = merged.merge(unemp, on=["Country Name", "Country Code", "Year"], how="outer")
merged = merged.merge(inflation, on=["Country Name", "Country Code", "Year"], how="outer")
merged = merged.merge(migration, on=["Country Name", "Country Code", "Year"], how="outer")
merged = merged.merge(population, on=["Country Name", "Country Code", "Year"], how="outer")
merged = merged.merge(migrant_stock, on=["Country Name", "Country Code", "Year"], how="outer")
merged = merged.merge(health_exp, on=["Country Name", "Country Code", "Year"], how="outer")
merged = merged.merge(education_exp, on=["Country Name", "Country Code", "Year"], how="outer")
merged = merged.merge(life_expectancy, on=["Country Name", "Country Code", "Year"], how="outer")
merged = merged.merge(gini_index, on=["Country Name", "Country Code", "Year"], how="outer")


# Deriving Migrant % of Population
merged["Migrant % of Population"] = (
    merged["Migrant Stock Total"] / merged["Total Population"]
) * 100

merged = merged.dropna(subset=["GDP"])

merged.to_csv("data/master_dataset_1980_2024.csv", index=False)
