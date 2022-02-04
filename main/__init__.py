import pandas as pd

from main.src.data_distribution_scopus import DataDistributionScopus
from main.src.data_distribution_wos import DataDistributionWos


def main():
    data_df_wos = pd.read_excel("data/wos2021.xls")
    data_df_scopus = pd.read_excel("data/Scopus2021.xlsx")
    dictionary_df = pd.read_excel("data/dictionary.xlsx")
    employees_df = pd.read_excel("data/Сотрудники.xls")
    wos = DataDistributionWos(dictionary_df, employees_df, data_df_wos)
    wos_dict = wos.count_data()
    scopus = DataDistributionScopus(dictionary_df, employees_df, data_df_scopus)
    scopus_dict = scopus.count_data()
    for keys, values in wos_dict.items():
        keys = keys.replace('"', '')
        values.to_excel(f"data/WoS {keys}.xlsx", index=False)
    for keys, values in scopus_dict.items():
        keys = keys.replace('"', '')
        values.to_excel(f"data/Scopus {keys}.xlsx", index=False)