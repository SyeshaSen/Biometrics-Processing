#!/usr/bin/env python3
"""
HW5: Fingerprint Processing - implement the `Fingerprint` class as described in README.md
"""
from typing import TypeVar

T = TypeVar(
    "T", bound="Fingerprint"
)  # Generic type that must be a subclass of Fingerprint


class Fingerprint:
    """Class to represent a fingerprint with associated metadata."""
    match_threshold: float = 0.9

    def __init__(
        self, data: list[list[str]], name: str, year: int, rows: int, cols: int
    ) -> None:
        """
        Initialize a Fingerprint object with the given data and metadata.

        Arguments:
            data (list[list[str]]): 2D list representing the fingerprint pixels
            name (str): Name associated with the fingerprint
            year (int): Year the fingerprint was recorded
            rows (int): Number of rows in the fingerprint data
            cols (int): Number of columns in the fingerprint data
        """
        copy_of_data = data[:]
        self._data = copy_of_data
        self._name = name
        self._year = year
        self._rows = rows
        self._cols = cols

    @classmethod
    def from_file(cls: type[T], filename: str) -> T:
        """
        Create a Fingerprint object by reading fingerprint data from the file."""
        with open(filename, "r", encoding="utf-8") as file:
            name = file.readline().strip()
            year = int(file.readline().strip())
            rows = int(file.readline().strip())
            cols = int(file.readline().strip())

            raw_data = file.read()
            filtered_chars = [ch for ch in raw_data if not ch.isspace()]

            data = [
                filtered_chars[i * cols : (i + 1) * cols] for i in range(rows)
            ]

        return cls(data, name, year, rows, cols)
    
    @property
    def image(self) -> str:
        return "\n".join("".join(row) for row in self._data)
    
    @property
    def rows(self) -> int:
        return self._rows
    
    @property
    def cols(self) -> int:
        return self._cols
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def year(self) -> int:
        return self._year
    
    def __str__(self) -> str:
        return f"Fingerprint for: {self.name}. Year recorded: {self.year}"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fingerprint):
            return False
        if not other.cols == self.cols:
            return False
        if not other.rows == self.rows:
            return False
        
        total_match = 0
        for row in range (self.rows):
            for col in range(self.cols):
                if self._data[row][col] == other._data[row][col]:
                    total_match += 1

        num_pix = self.rows*self.cols

        matching = total_match/num_pix

        if matching >= self.match_threshold:
            return True