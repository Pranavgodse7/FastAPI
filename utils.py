import pandas as pd

EXCEL_PATH = "Data/capbudg.xls"


def load_excel_file(path=EXCEL_PATH):
    try:
        return pd.read_excel(path, sheet_name=None, engine='xlrd')
    except Exception as e:
        raise RuntimeError(f"Error loading Excel file: {e}")


def get_table_names():
    excel_data = load_excel_file()
    return list(excel_data.keys())


def get_row_names(table_name: str):
    excel_data = load_excel_file()
    if table_name not in excel_data:
        raise ValueError("Table not found.")
    df = excel_data[table_name]
    if df.empty:
        return []
    return df.iloc[:, 0].dropna().astype(str).tolist()


def calculate_row_sum(table_name: str, row_name: str):
    excel_data = load_excel_file()
    if table_name not in excel_data:
        raise ValueError("Table not found.")
    df = excel_data[table_name]

    target_row = df[df.iloc[:, 0].astype(str).str.strip() == row_name.strip()]

    if target_row.empty:
        raise ValueError("Row not found.")

    # Sum all numeric columns in the row (excluding first column)
    numeric_data = pd.to_numeric(target_row.iloc[0, 1:], errors='coerce')
    return numeric_data.sum(skipna=True)
