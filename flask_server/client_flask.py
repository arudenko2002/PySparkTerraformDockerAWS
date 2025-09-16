import requests
import json
import pyodbc

connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=DESKTOP-G229R30\SQLEXPRESS;"
                            "Database=probe;"
                            "Trusted_Connection=yes;")
page_size = 3
page=1
r = requests.get(f"http://localhost:8080/pages/?page={page}")
data = r.json()
pages = int(data["pages"])
result = json.loads(data['page'])
print(page, result)
for page in range(2, pages+1):
    r = requests.get(f"http://localhost:8080/pages/?page={page}")
    data = r.json()
    l = json.loads(data['page'])
    print(page, l)
    result += l
print(result)