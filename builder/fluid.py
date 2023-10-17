from typing import List

from builder.models import Contribution, Paper


class PaperFluidBuilder:
    """
    A fluid builder for paper
    No order is enforced
    """

    def __init__(self):
        self.title = None
        self.doi = None
        self.abstract = None
        self.authors = []
        self.contributions = []

    def add_title(self, title: str) -> 'PaperFluidBuilder':
        """
        add title to the paper
        :param title: the title of the paper
        :return: the builder for chaining
        """
        self.title = title
        return self

    def add_doi(self, doi: str) -> 'PaperFluidBuilder':
        """
        add doi to the paper
        :param doi: the doi of the paper
        :return: the builder for chaining
        """
        self.doi = doi
        return self

    def add_abstract(self, abstract: str) -> 'PaperFluidBuilder':
        """
        add abstract to the paper
        filters something like "yaser"
        :param abstract: the abstract of the paper
        :return: the builder for chaining
        :raises ValueError: if the abstract contains "yaser"
        """
        if "yaser" in abstract:
            raise ValueError("yaser is not allowed in abstract")
        self.abstract = abstract
        return self

    def add_author(self, author: str) -> 'PaperFluidBuilder':
        """
        add author to the paper
        :param author: the author of the paper
        :return: the builder for chaining
        """
        self.authors.append(author)
        return self

    def add_authors(self, authors: List[str]) -> 'PaperFluidBuilder':
        """
        add a set of authors to the paper
        :param authors: the authors of the paper
        :return: the builder for chaining
        """
        self.authors.extend(authors)
        return self

    def add_contribution(self, contribution: Contribution) -> 'PaperFluidBuilder':
        """
        add a contribution to the paper
        :param contribution: the contribution to add
        :return: the builder for chaining
        """
        self.contributions.append(contribution)
        return self

    def add_contributions(self, contributions: List[Contribution]) -> 'PaperFluidBuilder':
        """
        add a set of contributions to the paper
        :param contributions: the contributions to add
        :return: the builder for chaining
        """
        self.contributions.extend(contributions)
        return self

    def build(self) -> Paper:
        """
        build the paper
        and checks for required fields
        :raises ValueError: if the title is not set
        :return: the built paper
        """
        if self.title is None:
            raise ValueError("title is required")
        return Paper(self.title, self.doi, self.abstract, self.authors, self.contributions)


if __name__ == '__main__':
    """
    A simple run of the fluid builder.
    The builder is not enforcing any order.
    And it is not enforcing any required fields.
    """
    paper = PaperFluidBuilder().add_title("title").add_doi("doi").add_abstract("abstract").add_author("author").add_contribution(Contribution("contribution")).build()
    print(paper)
