from fastapi import FastAPI
import sys

app = FastAPI()
version = "{0}.{1}".format(sys.version_info.major, sys.version_info.minor)

@app.get('/')
async def index():
    return "Hello, World! From FastAPI with Hypercorn. On Python {}".format(version)
