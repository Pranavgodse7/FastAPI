
# 📊 Excel API with FastAPI

This FastAPI project allows users to upload an Excel file and interact with it through API endpoints. You can:

- List all tables in the Excel file.
- Retrieve row names from a specified table.
- Get the sum of numerical values in a specific row.

## 🚀 Features

- **List Tables**: Retrieve all table/sheet names in the Excel file.
- **Get Table Details**: Get the names of rows (first column values) from a specific table.
- **Row Sum**: Calculate the sum of values in a specific row.

---

## 🔁 Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Pranavgodse7/FastAPI.git
cd excel_api
```

### 2. Create and activate a virtual environment (recommended)

Using Conda:

```bash
conda create -n iris python=3.10 -y
conda activate iris
```

Or using `venv`:

```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn main:app --reload --port 9090
```

---

## 📫 API Endpoints

### a. GET `/list_tables`

- **Functionality**: Lists all table/sheet names from the Excel file.
- **Example Response**:

```json
{
  "tables": ["Initial Investment", "Revenue Projections", "Operating Expenses"]
}
```

---

### b. GET `/get_table_details?table_name=<TABLE_NAME>`

- **Query Parameter**:
  - `table_name`: Name of the table/sheet.
- **Functionality**: Returns first-column values (row names) from the table.
- **Example**:

```json
{
  "table_name": "Initial Investment",
  "row_names": [
    "Initial Investment=",
    "Opportunity cost (if any)="
  ]
}
```

---

### c. GET `/row_sum?table_name=<TABLE_NAME>&row_name=<ROW_NAME>`

- **Query Parameters**:
  - `table_name`: Name of the table.
  - `row_name`: The row label (must exist in first column).
- **Functionality**: Sums numerical values in the specified row.
- **Example**:

```json
{
  "table_name": "Initial Investment",
  "row_name": "Tax Credit (if any )=",
  "sum": 10
}
```

---

## 📬 Postman Collection

You can use the provided Postman collection `excel_api_collection.json` to test all the endpoints. Import it into Postman and make GET requests to:

- `http://localhost:9090/list_tables`
- `http://localhost:9090/get_table_details?table_name=YourTableName`
- `http://localhost:9090/row_sum?table_name=YourTableName&row_name=YourRowName`

---

## 🧠 Future Improvements

- Support for multiple Excel file formats (.xls, .csv).
- File upload via POST and session-based Excel tracking.
- Error handling enhancements and advanced row filtering.
- Integration with a simple frontend UI.

---

## 📄 License

This project is for demonstration purposes and does not carry a formal license.

---
