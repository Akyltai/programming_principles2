import re
import json

def normalize_price(price_str):
    return float(price_str.replace(" ", "").replace(",", "."))

with open(r"Practice_5/raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

#1. Extract all prices

price_pattern = r"\d[\d ]*,\d{2}"
all_prices_raw = re.findall(price_pattern, text)
all_prices = [normalize_price(p) for p in all_prices_raw]


#2. Find all product names

product_pattern = r"\d+\.\n(.+)"
product_names = re.findall(product_pattern, text)


#3. Calculate total amount

item_total_pattern = r"x [\d ]+,\d{2}\n([\d ]+,\d{2})"
item_totals_raw = re.findall(item_total_pattern, text)
item_totals = [normalize_price(t) for t in item_totals_raw]

calculated_total = sum(item_totals)


#4. Extract date and time

datetime_pattern = r"Время:\s(\d{2}\.\d{2}\.\d{4})\s(\d{2}:\d{2}:\d{2})"
datetime_match = re.search(datetime_pattern, text)

date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None


#5. Find payment method

payment_pattern = r"(Банковская карта|Наличные)"
payment_match = re.search(payment_pattern, text)

payment_method = payment_match.group(1) if payment_match else None


#6. Structured output (JSON)

result = {
    "product_names": product_names,
    "all_prices": all_prices,
    "calculated_total": calculated_total,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(result, ensure_ascii=False, indent=4))