import pandas as pd

def categorize_age(age):
    """Categorize individuals based on their age."""
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age <= 12:
        return 'Child'
    elif age <= 19:
        return 'Teen'
    elif age <= 64:
        return 'Adult'
    else:
        return 'Senior'

def categorize_individuals(file_path):
    """Categorize individuals from a CSV file based on their age."""
    df = pd.read_csv(file_path)
    df['Category'] = df['Age'].apply(categorize_age)
    return df

if __name__ == "__main__":
    file_path = '../data/individuals.csv'
    categorized_df = categorize_individuals(file_path)
    print(categorized_df)