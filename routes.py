from sre_constants import SUCCESS
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from os import getcwd, remove
from numpy import float64
import pandas as pd


router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(getcwd() + "/" + file.filename, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return"success"

@router.get("/file/{name_file}")
def get_file(name_file: str):
    return FileResponse(getcwd() + "/" + name_file)

@router.get("/download/{name_file}")
def download_file(name_file: str):
    return FileResponse(getcwd() + "/" + name_file, media_type="application/octet-stream", filename=name_file)


@router.get("/predictions/{name_file}")
def predictions_file(name_file: str,ds: str  , y: str):
    
    df = pd.read_csv(getcwd() + "/" + name_file)
    print(df.info)

    type(df.columns)

    print(list(df.columns))

    lista=list(df.columns)

    lista.remove(ds)

    lista.remove(y)

    df.drop(lista, axis = 'columns', inplace=True)

    print(df.info)

    df = df.rename(columns={y:"y",ds:"ds"})

    df = df.astype ({"ds": "datetime64","y": "float64"})

    df = df.dropna()

   
    return SUCCESS