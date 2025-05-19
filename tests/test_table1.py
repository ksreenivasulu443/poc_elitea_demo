import pytest
import pandas as pd
import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.abspath(os.path.join(base_dir,'data', "Clinical_Data_Validation_Cohort.xlsx"))



@pytest.fixture(scope='module')
def read_data():
    df = pd.read_excel(file_path)
    return df

def test_age_category_childhood(read_data):
    clinical_df = read_data
    """TC_01: Verify age category for age less than 12."""
    patient = clinical_df[clinical_df['Age'] < 12].iloc[0]
    assert patient['Age_Category'] == 'Childhood', (
        f"Expected 'Childhood' but got '{patient['Age_Category']}' for Patient ID {patient['Patient ID']}"
    )


def test_age_category_teenage(read_data):
    """TC_02: Verify age category for age between 12 and 20."""
    clinical_df = read_data
    patient = clinical_df[(clinical_df['Age'] >= 12) & (clinical_df['Age'] <= 20)].iloc[0]
    assert patient['Age_Category'] == 'Teenage', (
        f"Expected 'Teenage' but got '{patient['Age_Category']}' for Patient ID {patient['Patient ID']}"
    )


def test_age_category_adult(read_data):
    """TC_03: Verify age category for age between 21 and 60."""
    clinical_df = read_data
    patient = clinical_df[(clinical_df['Age'] >= 21) & (clinical_df['Age'] <= 60)].iloc[0]
    assert patient['Age_Category'] == 'Adult', (
        f"Expected 'Adult' but got '{patient['Age_Category']}' for Patient ID {patient['Patient ID']}"
    )


def test_age_category_old(read_data):
    """TC_04: Verify age category for age above 60."""
    clinical_df = read_data
    patient = clinical_df[clinical_df['Age'] > 60].iloc[0]
    assert patient['Age_Category'] == 'Old', (
        f"Expected 'Old' but got '{patient['Age_Category']}' for Patient ID {patient['Patient ID']}"
    )
