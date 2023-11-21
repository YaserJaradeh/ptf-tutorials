from typing import List

from modular.common import fetch_papers_from_source
from modular.common import fetch_papers_from_arxiv, fetch_papers_from_nips, fetch_papers_from_springer


def collect_papers(sources: List):
    for source in sources:
        fetch_papers_from_source(source)


def collect_papers_various_sources(sources: List):
    for source in sources:
        if source == "arxiv":
            fetch_papers_from_arxiv("cs")
        elif source == "nips":
            fetch_papers_from_nips()
        elif source == "springer":
            fetch_papers_from_springer("jmlr", 2019)
        else:
            raise ValueError(f"Unknown source {source}")


if __name__ == "__main__":
    collect_papers(["arxiv", "nips", "springer"])
