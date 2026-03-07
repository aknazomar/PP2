import re
import json

# Load receipt text
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# -----------------------------
# Extract all prices
# -----------------------------
price_pattern = r"\d{1,3}(?: \d{3})*,\d{2}"
prices = re.findall(price_pattern, text)

# -----------------------------
# Extract product names
# -----------------------------
product_pattern = r"\d+\.\n(.+)"
products = re.findall(product_pattern, text)

# Clean product names
products = [p.strip().replace("\n", " ") for p in products]

# -----------------------------
# Extract total amount
# -----------------------------
total_match = re.search(r"ИТОГО:\s*\n?([\d ]+,\d{2})", text)
total_amount = total_match.group(1) if total_match else None

# -----------------------------
# Extract date and time
# -----------------------------
datetime_match = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})", text
)

date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None

# -----------------------------
# Extract payment method
# -----------------------------
payment_match = re.search(r"(Банковская карта|Наличные)", text)
payment_method = payment_match.group(1) if payment_match else None

# -----------------------------
# Structured output
# -----------------------------
data = {
    "products": products,
    "prices": prices,
    "total_amount": total_amount,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(data, indent=4, ensure_ascii=False))