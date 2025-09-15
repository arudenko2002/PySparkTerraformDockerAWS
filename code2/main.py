import uvicorn
import argparse
from fastapi import FastAPI, BackgroundTasks
import asyncio
from fastapi.responses import HTMLResponse
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: list[str or AnyHttpUrl] = ['http://localhost:8000']
    # OPENAPI_CLIENT_ID: str = ""
    # APP_CLIENT_ID: str = ""
    # TENANT_ID: str = ""
    FUNC: str = ""

    class Config:
        env_file = 'config.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True

settings = Settings()

# creating a FastAPI app
app = FastAPI(title='FastApi Example')

# @app.get("/")
# async def root(background_tasks: BackgroundTasks):
#     background_tasks.add_task(my_background_task)
#     return {"message": "Hello, world!"}
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.get('/')
async def home():
    data = "hello world"
    return {'data': data}

# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.get('/home/{num}')
async def disp(num: int):
    return {'data': num ** 2}

@app.get('/func/', response_class=HTMLResponse)
async def func2(N: str):
    func = settings.FUNC
    array = N
    #func = request.args.get('func', None) # &func=max
    array2 = [int(x) for x in array.split()]
    if func == "max":
        rez = max(array2)
    elif func=="min":
        rez = min(array2)
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

#  To ensure that the server shutdown is complete we add these code:
background_tasks = set()

async def my_background_task():
    try:
        while True:
            await asyncio.sleep(1)
            # print("Background task running...")
    except asyncio.CancelledError:
        print("Background task cancelled")

@app.on_event("startup")
async def startup_event():
    task = asyncio.create_task(my_background_task())
    background_tasks.add(task)

@app.on_event("shutdown")
async def shutdown_event():
    for task in background_tasks:
        task.cancel()
    await asyncio.gather(*background_tasks, return_exceptions=True)
    print("Server shutting down...")

def func1():
    if args.aggregate.lower() == "max":
        r = max(args.numbers)
    elif args.aggregate.lower() == "min":
        r = min(args.numbers)
    elif args.aggregate.lower() == "sum":
        r = sum(args.numbers)
    else:
        r = "unknown command"
    print(r)

def func2(port, func):
    print(port, func)
    uvicorn.run('main:app', host='0.0.0.0', port=int(port), reload=True)
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example program with flags')
    parser.add_argument('--aggregate', type=str, help='aggregate function sum|max|min')
    parser.add_argument('--port', type=int, help='Port for flask server')
    parser.add_argument('numbers', nargs="*", type=int, help="Array of numbers to aggregate")
    args = parser.parse_args()
    if args.port:
        func2(args.port,args.aggregate)
    elif len(args.numbers)>0:
        func1()
    else:
        print("unknown command")
        pass






