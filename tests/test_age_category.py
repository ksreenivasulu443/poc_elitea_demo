import pytest
import pandas as pd

# Sample function to categorize age

def categorize_age(age):
    if age < 12:
        return "Childhood"
    elif 12 <= age <= 20:
        return "Teenage"
    elif 21 <= age <= 60:
        return "Adult"
    else:
        return "Old"

# Test cases

def test_age_category_childhood():
    assert categorize_age(10) == "Childhood"

def test_age_category_teenage():
    assert categorize_age(15) == "Teenage"

def test_age_category_adult():
    assert categorize_age(30) == "Adult"

def test_age_category_old():
    assert categorize_age(65) == "Old"
