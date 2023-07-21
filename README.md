Exchange Rates Retrieval Tool
This is a Python console utility that fetches exchange rates for specific currencies from the PrivatBank public API for a given number of days. It utilizes the aiohttp library for asynchronous network requests to retrieve the data in parallel.

Requirements
Python 3.7 or higher
Installation
Clone the repository or download the code files.

Install the required dependencies using pip:

Copy code
pip install aiohttp
Usage
Open a terminal or command prompt in the directory where the code is located.

Run the script using the following command:

Copy code
python exchange_rates.py
The utility will prompt you to enter the number of days for which you want to check the exchange rates. Please enter a valid integer between 1 and 10.

Next, you will be asked to enter the additional currencies you want to check, separated by spaces (e.g., USD EUR PLN). Supported currencies are: USD, EUR, PLN, AZN, CAD, CNY, DKK, GBP, HUF, JPY, MDL, SGD, TRY, BYN, AUD, CHF, CZK, ILS, KZT, NOK, TMT, UZS, GEL, UAH.

The utility will display the exchange rates for the specified currencies over the selected number of days.
