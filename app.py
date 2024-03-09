from scripts.data_loader import load_data

def run_app(file_name):
    data = load_data(file_name)
    print(data)

if __name__ == "__main__":
    file_name = "data/happiness_report.csv"
    run_app(file_name)
