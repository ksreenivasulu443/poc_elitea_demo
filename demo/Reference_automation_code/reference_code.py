import pytest
import pandas as pd

# ========= Constants ============
SOURCE_PATH = "C:/Users/shikrapla_thippeswam/PycharmProjects/pytest/data/Clinical_Data_Validation_Cohort.csv"
TARGET_PATH = "C:/Users/shikrapla_thippeswam/PycharmProjects/pytest/Verify/age_category_data.csv"


# ========= Functions ============

def load_data(source_path, target_path):
    """
    Loads source and target data from the provided paths.
    """
    df1 = pd.read_csv(source_path)
    df2 = pd.read_csv(target_path)
    return df1, df2


def merge_data(source_df, target_df, join_column="Patient ID"):
    """
    Merges source and target data on the specified column.
    """
    return pd.merge(source_df, target_df, on=join_column, how="inner")


def compute_age_category(age):
    """
    Computes age category based on the age column.
    """
    if age <= 11:
        return "Childhood"
    elif 12 <= age <= 20:
        return "Teenage"
    elif 21 <= age <= 60:
        return "Adult"
    else:
        return "Old"


def process_data(merged_df):
    """
    Processes data to compute age categories and check category matching.
    """
    # Compute the computed age category column
    merged_df["Computed Age Category"] = merged_df["Age"].apply(compute_age_category)

    # Add a flag column for category matching
    merged_df["Category Match"] = merged_df["Computed Age Category"] == merged_df["Age Category"]

    return merged_df


def validate_data(merged_df):
    """
    Validates that all rows have matching categories.
    Returns a boolean indicating success.
    """
    return merged_df["Category Match"].all()


# ========= Tests ============

@pytest.fixture
def setup_data():
    """
    Fixture to prepare and process data for testing.
    """
    source_df, target_df = load_data(SOURCE_PATH, TARGET_PATH)
    merged_df = merge_data(source_df, target_df)
    processed_df = process_data(merged_df)
    return processed_df


def test_category_match(setup_data):
    """
    Test to ensure every computed age category matches the target age category.
    """
    processed_df = setup_data
    assert validate_data(processed_df), "Computed age categories do not match Age Categories in some rows."


"""
Run the pytest command from the terminal:
pytest -v
"""
