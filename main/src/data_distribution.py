from pandas import DataFrame


class DataDistribution:
    def __init__(self, dictionary_df: DataFrame, employees_df: DataFrame, data_df: DataFrame):
        self.dictionary_df = dict(zip(dictionary_df["Сотрудник"].to_list(), dictionary_df["names"].to_list()))
        self.employees = employees_df
        self.data_df = data_df

    def find_in_dictionary(self, names: str):
        for keys, values in self.dictionary_df.items():
            if values.find(names.lower()) != -1:
                return keys
        else:
            return None

    def get_employees_dict(self) -> dict:
        department_list = self.employees["Подразделение"].to_list()
        names_list = self.employees["ФИО"].to_list()
        result_dict = {}
        tmp_dict = {}
        for i in range(len(department_list)):
            if department_list[i].find("Кафедра") != -1:
                if tmp_dict.get(department_list[i]):
                    tmp_dict[department_list[i]].append(names_list[i])
                else:
                    tmp_dict |= {department_list[i]: [names_list[i]]}
        for key, value in tmp_dict.items():
            result_dict |= {key: list(set(value))}
        return result_dict

    def get_article_list(self):
        pass

    def count_data(self):
        pass

