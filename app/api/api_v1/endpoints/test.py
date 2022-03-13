import os
from typing import Any

from fastapi import APIRouter, Depends,File, UploadFile
from pydantic.networks import EmailStr

from app import models, schemas
from app.api import deps
from app.models import ImageField

router = APIRouter()




@router.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@router.post("/uploadfile/")
async def create_upload_file(image: UploadFile= File(...),current_user: models.User = Depends(deps.get_current_active_user)):
    print(image.file)
    try:
        os.mkdir("images")
        print(os.getcwd())
    except Exception as e:
        print(e)
    file_name = os.getcwd() + "/"+ImageField.Meta.path+"/" + image.filename.replace(" ", "-")
    with open(file_name, 'wb+') as f:
        f.write(image.file.read())
        f.close()
    new_image = ImageField(filename=image.filename.replace(" ", "-"),url="/test_image")
    return {"filename": new_image.filename}

