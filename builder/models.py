from dataclasses import dataclass
from typing import List


@dataclass
class Contribution:
    name: str


@dataclass
class Paper:
    title: str
    doi: str
    abstract: str
    authors: List[str]
    contributions: List[Contribution]
