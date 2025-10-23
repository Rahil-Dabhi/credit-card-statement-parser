# Universal Credit Card Statement Parser

This repo contains a universal parser that extracts structured JSON from any bank credit-card statement PDF (text or scanned) and exposes a FastAPI endpoint /parse that accepts a PDF and returns JSON.

Run locally:
pip install -r requirements.txt
uvicorn app:app --reload
