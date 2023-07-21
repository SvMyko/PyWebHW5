# **Exchange Rates Retrieval Tool**

This is a Python console utility that fetches exchange rates for specific currencies from the PrivatBank public API for a given number of days. It utilizes the aiohttp library for asynchronous network requests to retrieve the data in parallel.

**Requirements:**
Python 3.7 or higher

**Installation:**
1. Clone the repository or download the code files.
2. Install the required dependencies using pip: _pip install aiohttp_

**Usage:**
1. Open a terminal or command prompt in the directory where the code is located.

2. Run the script using the following command: _python PyWebHW5.py_

The utility will prompt you to enter the number of days for which you want to check the exchange rates. Please enter a valid integer between 1 and 10.
Next, you will be asked to enter the additional currencies you want to check, separated by spaces (e.g., USD EUR PLN).

Supported currencies are: USD, EUR, PLN, AZN, CAD, CNY, DKK, GBP, HUF, JPY, MDL, SGD, TRY, BYN, AUD, CHF, CZK, ILS, KZT, NOK, TMT, UZS, GEL, UAH.

The utility will display the exchange rates for the specified currencies over the selected number of days.
