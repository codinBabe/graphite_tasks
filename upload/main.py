import cloudinary
import cloudinary.uploader
import os
from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
from uuid import uuid4
 
app = FastAPI()
load_dotenv()

cloudinary.config(
    cloud_name= 'dg8gy1yeq',
    api_key = os.getenv('API_KEY'),
    api_secret= os.getenv('API_SECRET'),
    secure=True
)

@app.get('/')
def home():
    return f"Hello World!"


@app.post("/upload_file")
def upload_file(file :UploadFile):
    if file:
        result = cloudinary.uploader.upload(
            file.file,
            asset_folder = 'upload', 
            public_id= str(uuid4()),
            overwrite = True,
            resource_type = 'image'
            )
        return result['secure_url']

