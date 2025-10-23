# app.py
import shutil
import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from parser_universal import parse_universal_credit_card_statement

app = FastAPI(title="Universal Credit Card Parser API")

@app.post("/parse")
async def parse_statement(file: UploadFile = File(...)):
    tmp_filename = f"tmp_{file.filename}"
    with open(tmp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        result = parse_universal_credit_card_statement(tmp_filename)
        os.remove(tmp_filename)
        return JSONResponse(content=result)
    except Exception as e:
        if os.path.exists(tmp_filename):
            os.remove(tmp_filename)
        return JSONResponse(content={"error": str(e)}, status_code=500)
