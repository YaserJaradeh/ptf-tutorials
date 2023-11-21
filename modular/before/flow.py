from unittest.mock import Mock

orkg = Mock()
orkg.get_papers = lambda: [Mock(content={"abstract": "This is an abstract"})]
open_ai = Mock()
open_ai.complete = lambda prompt, max_tokens: "Keywords:\nHere is a list of keywords\nKeyword1\nKeyword2\nKeyword3\n"
logger = Mock()


def extract_keywords_from_abstracts():
    # Get the abstracts
    for paper in orkg.get_papers():
        abstract = paper.content["abstract"]
        # Set up openAI connection
        open_ai.api_key = "123"
        prompt = f"Extract keywords from the following abstract:\n{abstract}\nKeywords:"
        # Call openAI
        keywords = open_ai.complete(prompt=prompt, max_tokens=10)
        # Clean up the keywords
        keywords = keywords.replace("Keywords:", "").strip().split("\n")
        if "here is a list of keywords" in keywords:
            keywords.remove("here is a list of keywords")
        keywords = [keyword.lower() for keyword in keywords]
        # Link to ORKG
        for keyword in keywords:
            entities = orkg.link_keyword_to_paper(keyword, paper)
            logger.DEBUG(entities, "entities.txt")
        logger.INFO(f"Linked {keywords} to {paper}")
        logger.DEBUG(keywords, "keywords.csv")


if __name__ == "__main__":
    extract_keywords_from_abstracts()
