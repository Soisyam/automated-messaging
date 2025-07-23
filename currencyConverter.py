import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if "rates" in data and target_currency in data["rates"]:
        return data["rates"][target_currency]
    else:
        print("Invalid currency code.")
        return None

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed. Please check currency codes.")

# Example Usage
amount = float(input("Enter amount: "))
base_currency = input("Enter base currency (e.g., INR): ").upper()
target_currency = input("Enter target currency (e.g., EUR): ").upper()

convert_currency(amount, base_currency, target_currency)
