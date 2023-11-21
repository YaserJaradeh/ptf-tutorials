def _get_abstracts():
    return []


def _get_keywords(abstracts):
    for abstract in abstracts:
        keywords = _call_openai_api(abstract)
        yield keywords


def _call_openai_api(abstract):
    return []


def _clean_keywords(keywords):
    return []


def _link_keywords_to_papers(keywords):
    return []


def _log_progress(keywords, entities):
    pass


def extract_keywords_from_abstracts():
    abstracts = _get_abstracts()
    keywords = _get_keywords(abstracts)
    keywords = _clean_keywords(keywords)
    entities = _link_keywords_to_papers(keywords)
    _log_progress(keywords, entities)


if __name__ == "__main__":
    extract_keywords_from_abstracts()
