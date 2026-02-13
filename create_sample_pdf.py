from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

file_path = "sample_income_statement.pdf"

doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()

content = []

# Title
content.append(Paragraph("<b>Sample Company Ltd</b>", styles["Title"]))
content.append(Paragraph("Income Statement (FY 2020 – FY 2025)", styles["Normal"]))
content.append(Spacer(1, 12))

# Table data (SHORTENED COLUMN HEADERS FOR PDF STABILITY)
table_data = [
    ["Particulars", "FY25", "FY24", "FY23", "FY22", "FY21", "FY20"],
    ["Revenue from operations", "204813", "163210", "133905", "89582", "65557", "72484"],
    ["Other income", "1212", "793.6", "388.49", "679", "369", "425.2"],
    ["Total Revenue", "206025", "164003.6", "134293.49", "90262", "65927", "72909"],

    ["Cost of materials consumed", "82937.43", "70264.61", "64170.92", "39689.13", "26885.09", "29395.56"],
    ["Excise Duty", "4736", "2784", "2174", "1350", "1056", "1188.8"],
    ["Purchases of stock-in-trade", "6859.21", "4626.96", "1885.71", "1654.69", "925.87", "4237.33"],
    ["Change in inventory", "-749", "-842.6", "-3445", "-997", "-171", "-1438"],

    ["Gross Profit", "112241.36", "87170.63", "69507.86", "48565.18", "37231.04", "39525.31"],
    ["Gross Margin", "0.5448", "0.5315", "0.5176", "0.5380", "0.5647", "0.5421"],

    ["Employee benefit expenses", "18850.26", "14465.87", "12166.42", "10076.99", "8897.36", "8108.15"],
    ["Other expenses", "45068.29", "35816.21", "29072.39", "21262.26", "15946.01", "16516.82"],

    ["EBITDA", "48322.81", "36888.55", "28269.05", "17225.93", "12387.67", "14900.34"],

    ["Finance costs", "4503.86", "2680.99", "1861.22", "1847.00", "2811.04", "3096.42"],
    ["Depreciation", "9473.86", "6809", "6171", "5312", "5287", "4886"],

    ["Profit Before Tax", "34330.31", "27393.77", "20236.77", "10066.93", "3624.63", "6960.92"],
    ["Tax Expense", "7988.04", "6375.47", "4735", "2605", "52", "2240.67"],
    ["Profit After Tax", "26342.27", "21018.30", "15501.77", "7461.93", "3572.63", "4720.25"],
]

table = Table(table_data, repeatRows=1)
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("GRID", (0,0), (-1,-1), 0.5, colors.black),
    ("ALIGN", (1,1), (-1,-1), "RIGHT"),
    ("ALIGN", (0,0), (0,-1), "LEFT"),
    ("FONT", (0,0), (-1,0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 6),
]))

content.append(table)

doc.build(content)

print("✅ PDF created successfully:", file_path)
