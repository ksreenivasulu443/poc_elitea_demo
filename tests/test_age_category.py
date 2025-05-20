import pytest
import pandas as pd

# Load the data files
clinical_data = pd.read_excel('Clinical_Data_Validation_Cohort.xlsx')
age_category_data = pd.read_csv('age_category_data.csv')

# Map the files based on 'Patient ID'
merged_data = pd.merge(clinical_data, age_category_data, on='Patient ID')

@pytest.mark.parametrize("age, expected_category", [
    (5, "Childhood"),
    (15, "Teenage"),
    (30, "Adult"),
    (65, "Old")
])
def test_age_category(age, expected_category):
    result = merged_data[merged_data['Age'] == age]['Age Category'].values[0]
    assert result == expected_category, f"Expected {expected_category} but got {result}"
