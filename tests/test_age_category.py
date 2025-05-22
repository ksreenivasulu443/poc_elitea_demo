import pytest
import pandas as pd
from src.age_category import compute_age_category

# Constants
SOURCE_PATH = "data/Clinical_Data_Validation_Cohort.csv"
TARGET_PATH = "data/age_category_data.csv"

# Functions

def load_data(source_path, target_path):
    df1 = pd.read_csv(source_path)
    df2 = pd.read_csv(target_path)
    return df1, df2

def merge_data(source_df, target_df, join_column="Patient ID"):
    return pd.merge(source_df, target_df, on=join_column, how="inner")

def process_data(merged_df):
    merged_df["Computed Age Category"] = merged_df["Age"].apply(compute_age_category)
    merged_df["Category Match"] = merged_df["Computed Age Category"] == merged_df["Age Category"]
    return merged_df

def validate_data(merged_df):
    return merged_df["Category Match"].all()

# Fixtures
@pytest.fixture
def setup_data():
    source_df, target_df = load_data(SOURCE_PATH, TARGET_PATH)
    merged_df = merge_data(source_df, target_df)
    processed_df = process_data(merged_df)
    return processed_df

# Tests

def test_verify_age_category_childhood(setup_data):
    processed_df = setup_data
    childhood_df = processed_df[processed_df["Age"] < 12]
    assert (childhood_df["Computed Age Category"] == "Childhood").all(), "Age category for age less than 12 is incorrect."

def test_verify_age_category_teenage(setup_data):
    processed_df = setup_data
    teenage_df = processed_df[(processed_df["Age"] >= 12) & (processed_df["Age"] <= 20)]
    assert (teenage_df["Computed Age Category"] == "Teenage").all(), "Age category for age between 12 and 20 is incorrect."

def test_verify_age_category_adult(setup_data):
    processed_df = setup_data
    adult_df = processed_df[(processed_df["Age"] >= 21) & (processed_df["Age"] <= 60)]
    assert (adult_df["Computed Age Category"] == "Adult").all(), "Age category for age between 21 and 60 is incorrect."

def test_verify_age_category_old(setup_data):
    processed_df = setup_data
    old_df = processed_df[processed_df["Age"] > 60]
    assert (old_df["Computed Age Category"] == "Old").all(), "Age category for age greater than 60 is incorrect."

def test_verify_invalid_age(setup_data):
    processed_df = setup_data
    invalid_age_df = processed_df[processed_df["Age"] < 0]
    assert (invalid_age_df["Computed Age Category"] == "").all(), "Age category for invalid age is incorrect."

def test_verify_missing_age(setup_data):
    processed_df = setup_data
    missing_age_df = processed_df[processed_df["Age"].isnull()]
    assert (missing_age_df["Computed Age Category"] == "").all(), "Age category for missing age is incorrect."

def test_verify_non_numeric_age(setup_data):
    processed_df = setup_data
    non_numeric_age_df = processed_df[pd.to_numeric(processed_df["Age"], errors='coerce').isnull()]
    assert (non_numeric_age_df["Computed Age Category"] == "").all(), "Age category for non-numeric age is incorrect."

def test_verify_patient_id_mapping(setup_data):
    processed_df = setup_data
    assert validate_data(processed_df), "Patient ID mapping is incorrect."
