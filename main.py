import requests
import re


import requests
import re


def fetch_and_save_wiki_text(title):
    response = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            "explaintext": True,
        },
    ).json()

    page = next(iter(response["query"]["pages"].values()))
    wiki_text = page["extract"]

    return wiki_text


city = "Tokyo"
info = fetch_and_save_wiki_text(city)


print(info)
