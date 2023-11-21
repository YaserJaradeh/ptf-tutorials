from typing import List
from modular.common import fetch_papers_from_source
from modular.common import fetch_papers_from_arxiv, fetch_papers_from_nips, fetch_papers_from_springer


def collect_papers(sources: List):
    map(fetch_papers_from_source, sources)


def collect_papers_various_sources(sources: List):
    map(_call_func_with_params, sources)


def _call_func_with_params(source: str):
    params = {
        "arxiv": ("cs",),
        "nips": None,
        "springer": ("jmlr", 2019)
    }
    functions = {
        "arxiv": fetch_papers_from_arxiv,
        "nips": fetch_papers_from_nips,
        "springer": fetch_papers_from_springer
    }
    if source not in functions:
        raise ValueError(f"Unknown source {source}")
    functions[source](*params[source]) if params[source] else functions[source]()


if __name__ == "__main__":
    collect_papers(["arxiv", "nips", "springer"])
