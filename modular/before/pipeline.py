from modular.common import (
    parse_document,
    preprocess_document,
    extract_metadata,
    build_knowledge_graph,
    extend_knowledge_graph,
    find_similar_documents
)


def process_document_pipeline(document_path: str):
    parsed_document = parse_document(document=document_path)
    preprocessed_document = preprocess_document(document=parsed_document)
    metadata = extract_metadata(document=preprocessed_document)
    knowledge_graph = build_knowledge_graph(metadata=metadata)
    augmented_knowledge_graph = extend_knowledge_graph(knowledge_graph=knowledge_graph)
    similar_documents = find_similar_documents(knowledge_graph=augmented_knowledge_graph)
    return similar_documents


if __name__ == "__main__":
    process_document_pipeline("document.pdf")

    find_similar_documents(
        knowledge_graph=extend_knowledge_graph(
            knowledge_graph=build_knowledge_graph(
                metadata=extract_metadata(
                    document=preprocess_document(
                        document=parse_document(
                            document="document.pdf"
                        )
                    )
                )
            )
        )
    )

