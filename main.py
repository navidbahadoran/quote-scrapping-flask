#!/usr/bin/env python
from flask import Flask
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)


def get_quote():
    response = requests.get('http://www.quotationspage.com/random.php').content
    soup = BeautifulSoup(response, 'lxml')
    quote = soup.find_all('dt', class_='quote')[0].text
    return quote


@app.route('/')
def home():
    return get_quote()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
