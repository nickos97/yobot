from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import os
from fastapi.responses import JSONResponse
from app.utils import Query
import json

app = FastAPI()

os.environ["OPENAI_API_KEY"] = os.environ.get('APIKEY') 
loader = TextLoader('app/schedules.txt')
index = VectorstoreIndexCreator().from_loaders([loader])


@app.get("/")
def read_root():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'views', 'page.html')
    return FileResponse(file_path)

@app.post("/promt")
async def promt(query: Query):
    try:
        for _ in range(10):
            response = index.query(query.question)
        return {"answer": response}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    