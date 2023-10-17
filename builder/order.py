from builder.models import Paper, Contribution


class ContributionBuilder:
    """
    A builder for contribution
    This is the second builder in the build order
    """
    paper_builder: 'PaperBuilder'

    def __init__(self, paper_builder: 'PaperBuilder'):
        """
        Store the first builder in the internal state
        NOTE: this will make the two builders tightly coupled
        :param paper_builder: the first builder
        """
        self.name = None
        self.paper_builder = paper_builder

    def add_name(self, name: str) -> 'ContributionBuilder':
        """
        add name to the contribution
        :param name: the name of the contribution
        :return: the builder for chaining
        """
        self.name = name
        return self

    def build(self) -> Paper:
        """
        build the paper.
        NOTE: this builder will need to know the internal state of the first builder
        :return: the built paper
        """
        return Paper(
            title=self.paper_builder.title,
            doi=self.paper_builder.doi,
            contributions=[Contribution(self.name)],
            abstract=None,
            authors=None
        )


class PaperBuilder:
    """
    A builder for paper
    This is the first builder in the build order
    It doesn't enforce any order on its methods, but it has no build method
    """

    def __init__(self):
        self.title = None
        self.doi = None

    def add_title(self, title: str) -> 'PaperBuilder':
        """
        add title to the paper
        :param title: the title of the paper
        :return: the builder for chaining
        """
        self.title = title
        return self

    def add_doi(self, doi: str) -> 'PaperBuilder':
        """
        add doi to the paper
        :param doi: the doi of the paper
        :return: the builder for chaining
        """
        self.doi = doi
        return self

    def content(self) -> ContributionBuilder:
        """
        This method is the bridge between the two builders
        It returns the second builder
        :return: the contribution builder (2nd builder)
        """
        return ContributionBuilder(self)


if __name__ == '__main__':
    print(PaperBuilder()
          .add_title("title")
          .add_doi("doi")
          .content()
          .add_name("name")
          .build())
