import pytest
from seq import calculate_statistics

def test_calculate_statistics():
    seq = "ACGTNNNN"
    stats, percentages, total = calculate_statistics(seq)
    assert stats == {"A": 1, "C": 1, "G": 1, "T": 1, "Unknown": 4}
    assert round(percentages["A"], 1) == 12.5
    assert total == 8

def test_empty_sequence():
    seq = ""
    stats, percentages, total = calculate_statistics(seq)
    assert stats == {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}
    assert total == 0
    assert percentages == {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}
