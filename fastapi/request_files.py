from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

# Upload File


@app.post("/upload-file/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# Optional File Upload


@app.post("/optional-upload-file/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}
