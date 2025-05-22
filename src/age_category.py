def compute_age_category(age):
    if age < 12:
        return "Childhood"
    elif 12 <= age <= 20:
        return "Teenage"
    elif 21 <= age <= 60:
        return "Adult"
    else:
        return "Old"