def parse_pdf_paper(paper):
    print(f"Parsing PDF paper {paper}")


def parse_html_paper(paper):
    print(f"Parsing HTML paper {paper}")


def parse_ocr_paper(paper):
    print(f"Parsing OCR paper {paper}")


def iterate_over_papers():
    papers = ["paper1.html", "paper2.pdf", "paper3.jpg"]
    for paper in papers:
        if paper.endswith(".pdf"):
            parse_pdf_paper(paper)
        elif paper.endswith(".html"):
            parse_html_paper(paper)
        elif paper.endswith(".jpg"):
            parse_ocr_paper(paper)
        else:
            raise ValueError(f"Unknown paper type {paper}")


if __name__ == "__main__":
    iterate_over_papers()
