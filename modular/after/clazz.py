from abc import ABC, abstractmethod


class PaperClass(ABC):
    @abstractmethod
    def parse(self):
        pass

    @classmethod
    def create(cls, paper) -> "PaperClass":
        if paper.endswith(".pdf"):
            return PdfPaper(paper)
        elif paper.endswith(".html"):
            return HtmlPaper(paper)
        elif paper.endswith(".jpg"):
            return OcrPaper(paper)
        else:
            raise ValueError(f"Unknown paper type {paper}")


class PdfPaper(PaperClass):
    def __init__(self, paper):
        self.paper = paper

    def parse(self):
        print(f"Parsing PDF paper {self.paper}")


class HtmlPaper(PaperClass):
    def __init__(self, paper):
        self.paper = paper

    def parse(self):
        print(f"Parsing HTML paper {self.paper}")


class OcrPaper(PaperClass):
    def __init__(self, paper):
        self.paper = paper

    def parse(self):
        print(f"Parsing OCR paper {self.paper}")


def iterate_over_papers():
    papers = ["paper1.html", "paper2.pdf", "paper3.jpg"]
    for paper in papers:
        PaperClass.create(paper).parse()


if __name__ == "__main__":
    iterate_over_papers()
