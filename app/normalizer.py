import re

STANDARD_MAP = {
    "revenue": "Revenue",
    "total revenue": "Revenue",
    "sales": "Revenue",
    "operating expenses": "Operating Expenses",
    "operating costs": "Operating Expenses",
    "net income": "Net Income",
    "profit": "Net Income"
}

def normalize_line_item(line):
    for key in STANDARD_MAP:
        if key in line.lower():
            value = extract_number(line)
            return STANDARD_MAP[key], value

    return "Unknown", None

def extract_number(text):
    match = re.findall(r"[-+]?\d[\d,]*\.?\d*", text)
    return match[-1] if match else None
