import sys
from fastapi import FastAPI

app = FastAPI()
version = "{0}.{1}".format(sys.version_info.major, sys.version_info.minor)

@app.get("/")
async def index():
    return "Hello, World from FastAPI. Running on Hypercorn and Python {}.".format(version)
