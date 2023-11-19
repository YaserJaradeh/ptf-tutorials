# This file contains common functions that are used by multiple modules

def fetch_papers_from_source(source: str):
    """
    Fetch papers from a source
    :param source: the source to fetch from
    :return: a list of papers
    """
    print(f"Collecting papers from {source}")


def fetch_papers_from_arxiv(arxiv_group: str):
    """
    Fetch papers from arxiv
    :param arxiv_group: the arxiv group to fetch from
    :return: a list of papers
    """
    print(f"Collecting papers from arxiv/{arxiv_group}")


def fetch_papers_from_nips():
    """
    Fetch papers from nips
    :return: a list of papers
    """
    print(f"Collecting papers from nips")


def fetch_papers_from_springer(journal_id: str, year: int):
    """
    Fetch papers from springer
    :param journal_id: the journal id to fetch from
    :param year: the year to fetch from
    :return: a list of papers
    """
    print(f"Collecting papers from springer/{journal_id}/{year}")


def parse_document(**kwargs):
    pass


def preprocess_document(**kwargs):
    pass


def extract_metadata(**kwargs):
    pass


def build_knowledge_graph(**kwargs):
    pass


def extend_knowledge_graph(**kwargs):
    pass


def find_similar_documents(**kwargs):
    pass
