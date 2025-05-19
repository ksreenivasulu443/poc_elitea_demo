import pytest
import pandas as pd
import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.abspath(os.path.join(base_dir,'data', "Clinical_Data_Validation_Cohort.xlsx"))


@pytest.fixture(scope='module')
def read_data():
    df = pd.read_csv(r"C:\Users\Sreenivasulu_Kattuba\Documents\poc_elitea_demo\data\Clinical_Data_Validation_Cohort.xlsx")
    return df

def test_age_category_childhood(read_data):
    clinical_df = read_data
    """TC_01: Verify age category for age less than 12."""
    patient = clinical_df[clinical_df['Age'] < 12].iloc[0]
    assert patient['Age Category'] == 'Childhood', (
        f"Expected 'Childhood' but got '{patient['Age Category']}' for Patient ID {patient['Patient ID']}"
    )


def test_age_category_teenage(clinical_df):
    """TC_02: Verify age category for age between 12 and 20."""
    patient = clinical_df[(clinical_df['Age'] >= 12) & (clinical_df['Age'] <= 20)].iloc[0]
    assert patient['Age Category'] == 'Teenage', (
        f"Expected 'Teenage' but got '{patient['Age Category']}' for Patient ID {patient['Patient ID']}"
    )


def test_age_category_adult(clinical_df):
    """TC_03: Verify age category for age between 21 and 60."""
    patient = clinical_df[(clinical_df['Age'] >= 21) & (clinical_df['Age'] <= 60)].iloc[0]
    assert patient['Age Category'] == 'Adult', (
        f"Expected 'Adult' but got '{patient['Age Category']}' for Patient ID {patient['Patient ID']}"
    )


def test_age_category_old(clinical_df):
    """TC_04: Verify age category for age above 60."""
    patient = clinical_df[clinical_df['Age'] > 60].iloc[0]
    assert patient['Age Category'] == 'Old', (
        f"Expected 'Old' but got '{patient['Age Category']}' for Patient ID {patient['Patient ID']}"
    )
