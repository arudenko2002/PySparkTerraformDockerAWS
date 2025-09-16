import os
import argparse
from flask import Flask, jsonify, request
import pyodbc

# creating a Flask app
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})

        # A simple function to calculate the square of a number


# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return {'data': num ** 2}

@app.route('/api/', methods=['GET'])
def api():
    array = request.args.get('urls', None)
    array2 = [x for x in array.split()]
    resp = []
    for n,ind in enumerate(array2):
        resp.append(ind+"_L"+str(n+1))
    return resp

@app.route('/func/', methods=['GET'])
def func2():
    # rez = str(func)
    func = os.environ['FUNC']
    array = request.args.get('N', None)
    #func = request.args.get('func', None) # &func=max
    array2 = [int(x) for x in array.split()]
    if func == "max":
        rez = max(array2)
    elif func=="sum":
        rez = sum(array2)
    else:
        rez = "unknown function"
    result = f"""
     <html>
 <head>
 <title>{func}</title>
 </head>
 <body>
 <p>{func}</p>
 <p>{rez}</p>
 </body>
 </html
    """

    return result


def call_ms_server(page):
    connection = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=192.168.1.65,1433;"  # comma between hostname and port
        "Database=Probe;"
        "UID=pyspark_user;"
        "PWD=pyspark2025;"
    )

    page_size = 3
    cursor = connection.cursor()

    sql = "select count(id) from id2"
    cursor.execute(sql)
    rows = []
    for row in cursor:
        rows.append(row)
    count = rows[0][0]
    pages = int(count / page_size) if count % page_size == 0 else int(count / page_size) + 1

    sql = f"select * from id2 order by id, value offset {(page-1)*page_size} rows fetch next {page_size} rows only"
    cursor.execute(sql)
    rez=[]
    for row in cursor:
        rez.append(row)
    return rez, pages


@app.route('/pages/', methods=['GET'])
def pages():
    pages=4
    pagen = request.args.get('page', None)
    page = int(pagen)
    rez, pages = call_ms_server(page)
    print(rez)
    rez2 = [[x[0], x[1]] for x in rez]
    response = {"page": str(rez2), "pages": pages}
    return response


# def func1():
#     if args.aggregate.lower() == "max":
#         r = max(args.numbers)
#     elif args.aggregate.lower() == "sum":
#         r = sum(args.numbers)
#     else:
#         print("unknown command")
#     print(r)

def func2(port, func):
    print(port, func)
    os.environ['FUNC']=func
    app.run(debug=True, host='0.0.0.0', port=int(port))
    pass

if __name__=="__main__":
    func2("5000", "sum")





