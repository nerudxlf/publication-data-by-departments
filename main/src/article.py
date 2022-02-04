class Article:
    def __init__(
            self,
            title: str,
            authors: str,
            source: str,
            document_type: str,
            publication_year: str,
            addresses: str,
    ):
        self.title = title
        self.authors = authors
        self.source = source
        self.document_type = document_type
        self.publication_year = publication_year
        self.addresses = addresses

    def get_authors_wos(self, ) -> list:
        return self.authors.split("; ")

    def get_author_scopus(self) -> list:
        return self.authors.split(", ")

    def __str__(self):
        return f"Title {self.title}\n" \
               f"Authors {self.authors}\n" \
               f"Source {self.source}\n" \
               f"Document Type {self.document_type}\n" \
               f"Addresses {self.addresses}\n" \
               f"Publication Year {self.publication_year}"

    def __repr__(self):
        return f"Title {self.title}\n" \
               f"Authors {self.authors}\n" \
               f"Source {self.source}\n" \
               f"Document Type {self.document_type}\n" \
               f"Addresses {self.addresses}\n" \
               f"Publication Year {self.publication_year}"

    def __iter__(self):
        for i in list(self.__dict__.values()):
            yield i
