import pytest
import pandas as pd
from src.categorize import categorize_age, categorize_individuals

def test_categorize_age():
    assert categorize_age(5) == 'Child'
    assert categorize_age(15) == 'Teen'
    assert categorize_age(30) == 'Adult'
    assert categorize_age(70) == 'Senior'
    with pytest.raises(ValueError):
        categorize_age(-1)

def test_categorize_individuals(tmpdir):
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [5, 15, 30, 70]}
    df = pd.DataFrame(data)
    file_path = tmpdir.join('individuals.csv')
    df.to_csv(file_path, index=False)

    categorized_df = categorize_individuals(file_path)
    expected_categories = ['Child', 'Teen', 'Adult', 'Senior']
    assert categorized_df['Category'].tolist() == expected_categories

if __name__ == "__main__":
    pytest.main()