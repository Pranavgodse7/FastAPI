import pandas as pd
import os

# Get absolute path to the Excel file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, "Data", "capbudg.xls")

def load_sheet_data():
    try:
        if not os.path.exists(EXCEL_PATH):
            raise FileNotFoundError(f"Excel file not found at path: {EXCEL_PATH}")

        # Detect file extension
        ext = os.path.splitext(EXCEL_PATH)[1].lower()

        if ext == ".xls":
            df = pd.read_excel(EXCEL_PATH, sheet_name="CapBudgWS", engine="xlrd", header=None)
        elif ext == ".xlsx":
            df = pd.read_excel(EXCEL_PATH, sheet_name="CapBudgWS", engine="openpyxl", header=None)
        else:
            raise ValueError("Unsupported Excel file type")

        return df
    except Exception as e:
        raise RuntimeError(f"Error loading Excel file: {e}")


def split_into_tables(df):
    tables = {}
    current_table = []
    table_id = 0
    for index, row in df.iterrows():
        if row.isnull().all():
            if current_table:
                table_df = pd.DataFrame(current_table).reset_index(drop=True)
                tables[f"Table_{table_id + 1}"] = table_df
                current_table = []
                table_id += 1
        else:
            current_table.append(row)

    if current_table:
        table_df = pd.DataFrame(current_table).reset_index(drop=True)
        tables[f"Table_{table_id + 1}"] = table_df

    return tables

def get_table_names():
    df = load_sheet_data()
    tables = split_into_tables(df)
    return list(tables.keys())

def get_row_names(table_name):
    df = load_sheet_data()
    tables = split_into_tables(df)

    if table_name not in tables:
        raise ValueError("Table not found.")

    table = tables[table_name]
    if table.empty:
        return []

    return table.iloc[:, 0].dropna().astype(str).tolist()

def calculate_row_sum(table_name, row_name):
    df = load_sheet_data()
    tables = split_into_tables(df)

    if table_name not in tables:
        raise ValueError("Table not found.")

    table = tables[table_name]
    target_row = table[table.iloc[:, 0].astype(str).str.strip() == row_name.strip()]
    if target_row.empty:
        raise ValueError("Row not found.")

    numeric_data = pd.to_numeric(target_row.iloc[0, 1:], errors='coerce')
    return numeric_data.sum(skipna=True)
