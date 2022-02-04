import pandas as pd

from main.src.article import Article
from main.src.data_distribution import DataDistribution


class DataDistributionWos(DataDistribution):
    def get_articles_list(self):
        articles_list = []
        titles_list = self.data_df["Article Title"].to_list()
        authors_list = self.data_df["Authors"].to_list()
        source_list = self.data_df["Source Title"].to_list()
        document_type_list = self.data_df["Document Type"].to_list()
        publication_year_list = self.data_df["Publication Year"].to_list()
        addresses_list = self.data_df["Addresses"].to_list()
        for i in range(len(titles_list)):
            article = Article(
                title=titles_list[i],
                authors=authors_list[i],
                source=source_list[i],
                document_type=document_type_list[i],
                publication_year=publication_year_list[i],
                addresses=addresses_list[i],
            )
            articles_list.append(article)
        return articles_list

    def count_data(self):
        result_dict_df = {}
        employees_dict = self.get_employees_dict()
        articles_list = self.get_articles_list()
        for keys, values in employees_dict.items():
            result_dict = {"Автор": [], "Title": [], "Authors": [], "Source Title": [], "Document Type": [],
                           "Publication Year": [], "Addresses": []}
            for article in articles_list:
                authors_from_article = article.get_authors_wos()
                for i in authors_from_article:
                    name = self.find_in_dictionary(i)
                    if not name or not (name in values):
                        continue
                    article_dict = vars(article)
                    result_dict["Автор"].append(name)
                    result_dict["Authors"].append(article_dict["authors"])
                    result_dict["Title"].append(article_dict["title"])
                    result_dict["Source Title"].append(article_dict["source"])
                    result_dict["Document Type"].append(article_dict["document_type"])
                    result_dict["Publication Year"].append(article_dict["publication_year"])
                    result_dict["Addresses"].append(article_dict["addresses"])
            department_df = pd.DataFrame({
                "Автор": result_dict["Автор"],
                "Title": result_dict["Title"],
                "Authors": result_dict["Authors"],
                "Source Title": result_dict["Source Title"],
                "Document Type": result_dict["Document Type"],
                "Publication Year": result_dict["Publication Year"],
                "Addresses": result_dict["Addresses"],
            })
            result_dict_df |= {keys: department_df}
        return result_dict_df
