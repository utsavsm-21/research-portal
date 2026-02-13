import pdfplumber
import pandas as pd
from pathlib import Path
import uuid

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent
TEMP_DIR = BASE_DIR / "temp"
TEMP_DIR.mkdir(exist_ok=True)

# Keywords typically found in Income Statements
KEYWORDS = [
    "revenue",
    "total revenue",
    "income",
    "sales",
    "cost",
    "expense",
    "operating",
    "profit",
    "loss",
    "ebit",
    "ebitda",
    "tax",
    "net"
]

def extract_income_statement(pdf_path: str) -> str:
    """
    Extracts income statement line items from a PDF and
    outputs a CSV file with structured data.

    Returns:
        Path to generated CSV file
    """

    extracted_rows = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):

            # Safely extract tables
            try:
                tables = page.extract_tables()
            except Exception:
                continue

            if not tables:
                continue

            for table in tables:
                if not table:
                    continue

                for row in table:
                    # Defensive checks
                    if not row or not row[0]:
                        continue

                    label = str(row[0]).strip()
                    label_lower = label.lower()

                    # Check if this row looks like income statement data
                    if any(keyword in label_lower for keyword in KEYWORDS):

                        values = []
                        for cell in row[1:]:
                            if cell:
                                values.append(str(cell).strip())

                        extracted_rows.append({
                            "Line Item": label,
                            "Values": " | ".join(values),
                            "Page Number": page_number
                        })

    # If nothing found, still return a visible output
    if not extracted_rows:
        extracted_rows.append({
            "Line Item": "NO INCOME STATEMENT DATA FOUND",
            "Values": "",
            "Page Number": ""
        })

    df = pd.DataFrame(extracted_rows)

    # Unique filename to avoid Windows / OneDrive lock issues
    output_path = TEMP_DIR / f"income_statement_{uuid.uuid4().hex}.csv"
    df.to_csv(output_path, index=False)

    return str(output_path)
