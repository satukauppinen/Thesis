
import sqlite3
import pandas as pd

db_path = "results/crawl-data.sqlite"
conn = sqlite3.connect(db_path)

# JavaScript call table
js_calls = pd.read_sql_query("SELECT * FROM javascript_call", conn)
js_calls.to_csv("results/javascript_calls.csv", index=False)

#  HTTP requests
http = pd.read_sql_query("SELECT * FROM http_requests", conn)
http.to_csv("results/http_requests.csv", index=False)

print("Export completed.")
