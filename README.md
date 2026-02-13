Research Portal – Financial Statement Extraction Tool
Overview

This project implements a minimal internal research portal where AI-assisted tools are used for structured research tasks, not as an open-ended chatbot.

The current implementation focuses on Option A: Financial Statement Extraction to Excel/CSV.

A researcher can:
Upload a financial document (PDF)
Run a predefined research tool
Receive a structured, analyst-usable output for further analysis
The emphasis is on reliability, transparency, and structured output, rather than performance or conversational AI.

Supported Research Tool
Financial Statement Extraction
Input
Annual report or financial statement in text-based PDF format
Income statement presented in tabular form

Output
CSV file containing extracted income statement line items
Ready for use in Excel or analytical workflows

End-to-End Flow
User uploads a PDF through a simple web interface
Backend ingests and processes the document
Financial tables are extracted from the PDF
Relevant income statement rows are identified
A structured CSV file is generated and returned to the user

Tech Stack
Backend: Python, FastAPI
PDF Processing: pdfplumber
Data Structuring: pandas
Frontend: HTML (minimal upload UI)
Deployment: Render (free tier)

Setup Environment (VS Code)
python -m venv venv
venv\Scripts\activate     # Windows
pip install fastapi uvicorn pdfplumber pandas openai python-multipart

Project Structure
research-portal/
│
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── extractor.py     # Financial table extraction logic
│   ├── normalizer.py    # (Optional) Line-item normalization
│   ├── llm_helper.py    # (Optional) LLM usage for classification
│
├── static/
│   └── index.html       # Document upload UI
│
├── temp/                # Runtime-generated files
├── requirements.txt
├── README.md

Design Decisions & Judgment Calls
How are line items extracted?
Uses table-based extraction (pdfplumber.extract_tables)
Avoids raw text parsing for financial data
Prevents numeric hallucination
Handling different line item names
Keyword-based matching is used to identify income statement rows
Variations such as “Revenue”, “Total Revenue”, “Income”, etc. are supported
The design allows extension to a normalization dictionary
Missing or ambiguous data
If no relevant data is found, the output CSV explicitly contains: NO INCOME STATEMENT DATA FOUND

Numeric reliability
Numeric values are never generated or inferred
Only values present in the document tables are extracted
Currency and units
Currency and units are not inferred
Analysts are expected to interpret units based on the source document

Multi-year data
All numeric columns present in the table (e.g., FY20–FY25) are extracted
Values are preserved as-is without aggregation or transformation

Deployment
The application is deployed using Render (free tier) and accessible via a public URL.

Deployment Features
Publicly accessible web interface
PDF upload support
CSV download output

Limitations (Explicit)
Only text-based PDFs are supported
(Scanned or image-only PDFs are not handled)

Complex or highly nested financial layouts may reduce extraction accuracy

Free hosting limitations:
File size: ~5–10 MB
Cold start latency on first request
These limitations are intentionally surfaced to ensure transparency for evaluators and analysts.

How to Test
Open the public deployment link
Upload a text-based income statement PDF
Download the generated CSV file
Open in Excel to review extracted data

Author Notes
This implementation is intentionally minimal and extensible, demonstrating how AI-powered research tools can be embedded into structured workflows rather than used as generic chat systems.
