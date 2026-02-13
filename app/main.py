from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
import shutil, uuid
from app.extractor import extract_income_statement

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
TEMP_DIR = BASE_DIR / "temp"
TEMP_DIR.mkdir(exist_ok=True)

@app.get("/")
def home():
    return FileResponse(BASE_DIR / "static" / "index.html")

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    pdf_path = TEMP_DIR / f"{uuid.uuid4()}.pdf"

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    csv_path = extract_income_statement(str(pdf_path))

    return FileResponse(csv_path, filename="income_statement.csv")
