#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import subprocess

url = "https://nepalicalendar.rat32.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
today_data = soup.find("div", id="aajakodin")

requirements = ["yr", "mth", "gate", "ekadashi"]
results = []

for requirement in requirements:
    data = today_data.find("div", id=requirement).text.replace("\xa0", " ").strip()
    results.append(data)

subprocess.run(["notify-send", f"{results[1]} {results[2].replace(" day", "")}, {results[0].replace(" Year", " B.S.")} ({results[3]})"])
