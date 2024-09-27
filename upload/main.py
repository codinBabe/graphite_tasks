import cloudinary
import cloudinary.uploader
from cloudinary import CloudinaryImage
import os
from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
import json
 
app = FastAPI()
load_dotenv()

cloudinary.config(
    cloud_name= 'dg8gy1yeq',
    api_key = os.getenv('API_KEY'),
    api_secret= os.getenv('API_SECRET'),
    secure=True
)

result = ""

@app.get('/')
def home():
    return f"Hello World!"


@app.post("/upload_file")
def upload_file(img_file: UploadFile):
    cloudinary.uploader.upload(img_file.file.read(), public_id=img_file.filename)
    url = CloudinaryImage(public_id=img_file.filename).build_url()

    IMAGEJSON = 'imgDB.json'
    id = 0

    try:
        with open(IMAGEJSON, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    id = len(data)
    data[id] = url
    data = json.dumps(data, indent=4)

    with open(IMAGEJSON, 'w') as file:
        file.write(data)
    
    return {
        'id': id,
        'url': url
    }

@app.get("/get_image/{id}")
def get_image(id):
    IMAGEJSON = 'imgDB.json'
    with open(IMAGEJSON, 'r') as file:
        data = json.load(file)
    return {
        'url': data[id]
    }
    