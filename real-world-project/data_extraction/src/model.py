"""
    Python Real-World Project
    Project 1: Data Extraction
"""
from dataclasses import dataclass
from typing import TypeAlias

@dataclass
class XYPair:
    x: str
    y: str

@dataclass
class SomeOtherStructure:
    x: list[str]
    y: list[str]

RawData: TypeAlias = XYPair | SomeOtherStructure