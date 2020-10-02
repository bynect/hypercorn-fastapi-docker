import sys
from fastapi import FastAPI

app = FastAPI()
version = "{0}.{1}".format(sys.version_info.major, sys.version_info.minor)

@app.get("/")
async def index():
    return "Hello, World. From a FastAPI app running on Hypercorn and Python {}.".format(version)
