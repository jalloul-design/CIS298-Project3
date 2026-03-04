# Bing - Python Dot Env

from dotenv import load_dotenv
import os

# PY4E - Web Networking Chapter
import urllib.request
import urllib.error
import json
# Bing - Python Dot Env
load_dotenv()  # Load environment variables from .env file

# Access variables
API_KEY = os.getenv('API_KEY')

print(f'API_KEY: {API_KEY}')

# From Mr.Charnesky Web API Video
def get_json_from_url(url):

    try:
        with urllib.request.urlopen(url) as response:

            if response.status != 200:
                print(f"HTTP Error: {response.status}")
                return None

            data = response.read().decode('utf-8')

            try:
                return json.loads(data)

            except json.decoder.JSONDecodeError as e:
                print(f"JSON Error: {e}")
                return None

    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")

    except Exception as e:
        print(f"Unknown Error: {e}")

    return None

url = f"https://api.massive.com/v3/reference/tickers?market=stocks&active=true&order=asc&limit=100&sort=ticker&apiKey={API_KEY}"

json_data = get_json_from_url(url)
if json_data is not None:
    print("Fetched JSON data successfully:")
    print(json.dumps(json_data, indent=4))
else:
    print("Failed to fetch data")


def save_stock(ticker,stock_data):
    #ChatGpt- how can I make a file that saved information by the user input for my stock api
    filename = "saved_stocks.json"
    try:
        with open(filename, 'w') as file:
            json.dump(stock_data, file, indent=4) # From Mr.Charnesky Video(Web API)
            file.write("")
        print(f"Stock Data Saved: {filename}")
    except Exception as e:
        print(f"File does not exist, could not save the data: {e}")

def menu():
    print("\nWelcome to the Stock Explorer Program:")
    print("1.Search To View Stocks")
    print("2.Save Stock information")
    print("3.Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        ticker = input("Enter stock ticker: ").upper()
        url = f"https://api.massive.com/v3/reference/tickers?ticker={ticker}&market=stocks&active=true&apiKey={API_KEY}"
        stock_data = get_json_from_url(url)
        if stock_data is not None:
            print("Stock Data:")
            print(json.dumps(stock_data, indent=4))
        else:
            print("Stock Ticker Does Not Exist")

    elif choice == "2":
        ticker = input("Enter stock ticker: ").upper()
        url = f"https://api.massive.com/v3/reference/tickers?ticker={ticker}&market=stocks&active=true&apiKey={API_KEY}"
        stock_data = get_json_from_url(url)
        if stock_data is not None:
            save_stock(ticker, stock_data)
        else:
            print("Failed To Save Data")
    elif choice == "3":
        print("Thank You For Using The Stock Explorer Program!")
        break