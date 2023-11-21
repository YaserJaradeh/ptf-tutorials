from modular.common import (
    parse_document,
    preprocess_document,
    extract_metadata,
    build_knowledge_graph,
    extend_knowledge_graph,
    find_similar_documents
)


class Step:
    def __init__(self, func):
        self.func = func

    def __call__(self, **kwargs):
        self.func(**kwargs)


class Pipeline:
    def __init__(self, **kwargs):
        self.steps = []
        self.kwargs = kwargs

    def add_step(self, step: Step):
        self.steps.append(step)

    def run(self):
        for step in self.steps:
            step(**self.kwargs)

    def __call__(self):
        self.run()


if __name__ == '__main__':
    pipeline = Pipeline(
        document_path="document.pdf",
        parse_mode="pdf",
        special_tokens=["[SEP]", "[CLS]"],
        ignore_tags=["<img>", "<table>"],
        metadata=["title", "authors", "abstract", "references"],
        predicate_label_template="koko-{}",
        similarity_method="cosine",
        similarity_threshold=0.8,
    )
    pipeline.add_step(Step(parse_document))
    pipeline.add_step(Step(preprocess_document))
    pipeline.add_step(Step(extract_metadata))
    pipeline.add_step(Step(build_knowledge_graph))
    pipeline.add_step(Step(extend_knowledge_graph))
    pipeline.add_step(Step(find_similar_documents))

    pipeline.run()

