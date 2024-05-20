from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated


app = FastAPI()

@app.post("/files/")
async def create_file(
    # file: Annotated[bytes | None, File(description="A file read as bytes")] = None,
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {"file_size": [len(file) for file in files]}
    # return {"file_size": len(file)}

@app.post("/uploadfiles/")
async def create_upload_file(
    files: Annotated[list[UploadFile], File(description="Multiple files as UploadFile")],
    # file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"file_size": [file.filename for file in files]}
    # return {"filename": file.filename}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)