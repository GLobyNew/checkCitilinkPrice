import requests
import os
import re
from dotenv import load_dotenv
load_dotenv()


# Tell site (Citilink) to use Ekaterinburg as city
cookies = {
    "_space": "ekat_cl"
}



def main():
    # Get URL from .env file and trying to request with cookies
    URL = os.getenv("URL")
    REQUEST_URL=os.getenv("REQUEST_URL")
    r = requests.get(URL, cookies=cookies)
    page = r.text
    price_Match = re.search(r"data-meta-price=\"([ \d]+)\"", page)
    price_Number = price_Match.group(1)
    actual_price = int("".join(price_Number.split()))

    # Read old price
    with open("value.txt", "r") as f:
        old_value = f.read()
    
    # Write new price if they are not equal and make request to Make
    if actual_price != int(old_value):
        with open("value.txt", "w") as f:
            f.write(str(actual_price))
        r_post = requests.post(REQUEST_URL, {"NewPrice" : actual_price})
        

if __name__ == '__main__':
    main() 