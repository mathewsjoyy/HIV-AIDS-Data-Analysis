import pandas as pd 
import requests as r

url = "https://en.wikipedia.org/wiki/List_of_countries_by_HIV/AIDS_adult_prevalence_rate"
req = r.get(url)

data_list = pd.read_html(req.text)
target_df = data_list[1]

target_df.columns = ["Country", "Adult Prevalence of HIV/AIDS", "Num of People with HIV/AIDS", "Annual Deaths from HIV/AIDS", "Year of Estimate"]
target_df = target_df[["Country", "Adult Prevalence of HIV/AIDS", "Num of People with HIV/AIDS", "Annual Deaths from HIV/AIDS"]]

target_df["Adult Prevalence of HIV/AIDS"] = target_df["Adult Prevalence of HIV/AIDS"].str.replace("\[.*]","")
target_df["Num of People with HIV/AIDS"] = target_df["Num of People with HIV/AIDS"].str.replace("\[.*]","")
target_df["Annual Deaths from HIV/AIDS"] = target_df["Annual Deaths from HIV/AIDS"].str.replace("\[.*]","")
target_df["Country"] = target_df["Country"].str.replace("\[.*]","")

target_df = target_df[target_df["Annual Deaths from HIV/AIDS"] != "-"]
target_df = target_df.drop(77)

target_df["Adult Prevalence of HIV/AIDS"] = target_df["Adult Prevalence of HIV/AIDS"].str.replace("-", "0.00%")

target_df["Num of People with HIV/AIDS"] = pd.to_numeric(target_df["Num of People with HIV/AIDS"])
target_df["Annual Deaths from HIV/AIDS"] = pd.to_numeric(target_df["Annual Deaths from HIV/AIDS"])

target_df["Adult Prevalence of HIV/AIDS"] = target_df["Adult Prevalence of HIV/AIDS"].str.rstrip('%').astype('float') / 100.0

target_df.to_excel(r"HIV_dataset.xlsx") # Excel version
