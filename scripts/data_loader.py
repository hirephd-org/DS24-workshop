import pandas as pd

def load_data(file_path):
    """Load the happiness report data into a pandas DataFrame."""
    return pd.read_csv(file_path)

if __name__ == "__main__":
    data = load_data("../data/happiness_report.csv")
    print(data.head())
