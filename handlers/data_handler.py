import pandas as pd


def get_eligible():
    yield_df, concessions_df = load_data()
    yield_eligible = filter_eligible(yield_df, "Yield PtP", 1)
    concessions_eligible = filter_eligible(concessions_df, "Concession Rate PtP", 1)
    eligible = get_final_eligible(yield_eligible, concessions_eligible)
    return eligible


def load_data():
    """Load yield and concessions data from CSV files."""
    yield_df = pd.read_csv("../csvs/yield.csv")
    concessions_df = pd.read_csv("../csvs/concessions.csv")
    return yield_df, concessions_df


def filter_eligible(df, column, threshold):
    """Filter a DataFrame to include only logins with a column
    value greater than or equal to a specified threshold."""
    return df[df[column] >= threshold]["Grading Associate Login"]


def get_final_eligible(yield_logins, concessions_logins):
    """Combine yield and concessions login lists and sort logins
    that appear in both (i.e., duplicates across the combined list)."""
    merged = pd.concat([yield_logins, concessions_logins], ignore_index=True)
    return sorted(set(merged[merged.duplicated(keep=False)]))
