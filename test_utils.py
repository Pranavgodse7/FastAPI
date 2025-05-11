from utils import get_table_names, get_row_names, calculate_row_sum

print("📄 Table Names:", get_table_names())

table = get_table_names()[0]
print(f"📌 Row Names in {table}:", get_row_names(table))

sample_row = get_row_names(table)[0]
print(f"➕ Sum of row '{sample_row}':", calculate_row_sum(table, sample_row))
