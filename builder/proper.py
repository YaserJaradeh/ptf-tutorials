from abc import ABC, abstractmethod
from dataclasses import dataclass


# To insure the order of the method call, we need to use the abstract class to define interfaces
# The order of the method call is:
# set_title -> set_doi -> set_author -> set_contribution -> build


class ITitleSetter(ABC):
    """
    The interface for setting the title which opens the door for the next method call
    The next method call is set_doi
    """
    @abstractmethod
    def set_title(self, title: str) -> 'IDoiSetter':
        pass


class IDoiSetter(ABC):
    """
    The interface for setting the doi which opens the door for the next method call
    The next method call is set_author
    """
    @abstractmethod
    def set_doi(self, doi: str) -> 'IAuthorSetter':
        pass


class IAuthorSetter(ABC):
    """
    The interface for setting the author which opens the door for the next method call
    The next method call is set_contribution
    """
    @abstractmethod
    def set_author(self, author: str) -> 'IContributionSetter':
        pass


class IContributionSetter(ABC):
    """
    The interface for setting the contribution which opens the door for the next method call
    The next method call is build
    """
    @abstractmethod
    def set_contribution(self, contribution: str) -> 'IPaperBuilder':
        pass


class IPaperBuilder(ABC):
    """
    The interface for building the paper
    """
    @abstractmethod
    def build(self):
        pass


@dataclass
class Paper:
    """
    Minimal data class for a paper just to show the result
    """

    title: str
    doi: str
    author: str
    contribution: str


class PaperBuilder(IPaperBuilder, ITitleSetter, IDoiSetter, IAuthorSetter, IContributionSetter):
    """
    The concrete class that implements the interfaces
    This class is responsible for organizing the methods and building the paper
    """

    def __init__(self):
        """
        Should not be called directly
        Only via the init class method
        """
        self.title = None
        self.doi = None
        self.author = None
        self.contribution = None

    @classmethod
    def init(cls) -> ITitleSetter:
        """
        Intended to be the first method to call
        which gives the first interface rather than using the __init__ method
        """
        return cls()

    def set_title(self, title: str) -> IDoiSetter:
        """
        Set the title and return the next interface
        :param title: the title of the paper
        :return: self as IDoiSetter
        """
        self.title = title
        return self

    def set_doi(self, doi: str) -> IAuthorSetter:
        """
        Set the doi and return the next interface
        :param doi: the doi of the paper
        :return: self as IAuthorSetter
        """
        self.doi = doi
        return self

    def set_author(self, author: str) -> IContributionSetter:
        """
        Set the author and return the next interface
        :param author: the author of the paper
        :return: self as IContributionSetter
        """
        self.author = author
        return self

    def set_contribution(self, contribution: str) -> IPaperBuilder:
        """
        Set the contribution and return the next interface
        :param contribution: the contribution of the paper
        :return: self as IPaperBuilder
        """
        self.contribution = contribution
        return self

    def build(self):
        """
        Build the paper
        """
        return Paper(self.title, self.doi, self.author, self.contribution)


if __name__ == '__main__':
    print(PaperBuilder()
          .init()
          .set_title("title")
          .set_doi("doi")
          .set_author("author")
          .set_contribution("contribution")
          .build())
