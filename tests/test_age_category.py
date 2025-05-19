import pytest

# Sample test data
age_data = {
    10: "Child",
    15: "Teen",
    25: "Young Adult",
    40: "Adult",
    60: "Senior",
    80: "Elderly"
}

@pytest.mark.parametrize("age, expected_category", age_data.items())
def test_age_category(age, expected_category):
    # Here you would call the function that categorizes age
    # For example: category = categorize_age(age)
    # assert category == expected_category
    assert True  # Placeholder assertion for demonstration
