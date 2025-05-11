import os

# Print current working directory and absolute Excel file path
print(f"Current Working Directory: {os.getcwd()}")
print(f"Excel File Absolute Path: {os.path.abspath('Data/capbudg.xls')}")
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from utils import get_table_names, get_row_names, calculate_row_sum

app = FastAPI(title="Excel Sheet Processor API")


# Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/list_tables")
def list_tables():
    try:
        tables = get_table_names()
        return {"tables": tables}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    try:
        rows = get_row_names(table_name)
        return {"table_name": table_name, "row_names": rows}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    try:
        result = calculate_row_sum(table_name, row_name)
        return {
            "table_name": table_name,
            "row_name": row_name,
            "sum": result
        }
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
