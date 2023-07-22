import aiohttp
import asyncio
from datetime import datetime, timedelta
import time


API_BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates"

supported_currencies = {
    "USD", "EUR", "PLN", "AZN", "CAD", "CNY", "DKK", "GBP", "HUF", "JPY", "MDL",
    "SGD", "TRY", "BYN", "AUD", "USD", "CHF", "CZK", "ILS", "KZT", "NOK", "TMT",
    "UZS", "GEL", "UAH"
}

BASE_PROMPT = f'This console utility is designed to display the exchange rate of currencies ' \
              f'for a specified number of days. List of supported currencies: \n{", ".join(supported_currencies)}'

async def fetch_exchange_rates(session, date):
    url = f"{API_BASE_URL}?date={date}"
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        else:
            raise ValueError(f"Failed to fetch exchange rates for date {date}. Status code: {response.status}")


def get_date_range(days):
    days = min(days, 10)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    return start_date, end_date


def format_currency(currency_data):
    currency = currency_data["currency"]
    purchase_rate = currency_data.get("purchaseRate", currency_data.get("purchaseRateNB"))
    sale_rate = currency_data.get("saleRate", currency_data.get("saleRateNB"))
    return f"{currency: <8} | {purchase_rate: <13} | {sale_rate: <9}"


def process_days_input():
    while True:
        try:
            days_to_check = int(input("Enter the number of days to check exchange rates (up to 10): "))
            if 0 < days_to_check <= 10:
                return days_to_check
            print("Number of days should be between 1 and 10. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def process_currency_input():
    while True:
        additional_currencies = input("Enter additional currencies (e.g., USD EUR PLN): ").split()
        additional_currencies = [currency.upper() for currency in additional_currencies]

        invalid_currencies = set(additional_currencies) - supported_currencies
        if invalid_currencies:
            print("The following currencies are unsupported:", ", ".join(invalid_currencies))
        else:
            return additional_currencies


def print_exchange_rates_table(exchange_rates_data, additional_currencies):
    print("Date:", exchange_rates_data["date"])
    print('''currency | Purchase rate | Sale rate''')
    for currency_data in exchange_rates_data["exchangeRate"]:
        currency_code = currency_data["currency"]
        if currency_code in additional_currencies:
            print(format_currency(currency_data))
    print("-"*35)


async def main():
    try:
        days_to_check = process_days_input()

        start_date, end_date = get_date_range(days_to_check)

        additional_currencies = process_currency_input()

        async with aiohttp.ClientSession() as session:
            tasks = [fetch_exchange_rates(session, date.strftime('%d.%m.%Y')) for date in
                     (start_date + timedelta(days=i) for i in range(days_to_check))]

            exchange_rates_results = await asyncio.gather(*tasks)

            for date, rates_data in zip((end_date - timedelta(days=i) for i in range(days_to_check)),
                                        exchange_rates_results):
                print_exchange_rates_table({"date": date.strftime('%d.%m.%Y'), "exchangeRate": rates_data["exchangeRate"]},
                                           additional_currencies)

    except aiohttp.ClientError as e:
        print(f"Network error occurred: {e}")
    except ValueError as e:
        print(f"Value error occurred: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")

def exit_handler():
    input_handler = input('Print "Continue" to continue using or push enter to close the program: ')

    if input_handler.lower() == "continue":
        print(BASE_PROMPT)
        asyncio.run(main())
        exit_handler()
    else:
        print("Exiting the program...")
        time.sleep(3)
        exit()


if __name__ == "__main__":
    print(BASE_PROMPT)
    asyncio.run(main())
    exit_handler()
