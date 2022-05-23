from flask import Flask, render_template

app = Flask(__name__)
from bs4 import BeautifulSoup  # 1. import Beautiful Soup
import requests  # 2 import requests

source = requests.get('http://quotes.toscrape.com/').text
#print (source)
soup = BeautifulSoup(source, 'lxml')

quote = soup.find('div', class_='quote')  # finding the first quote text
quotetext = quote.span.text

author = soup.find('small', class_='author')  # finding the first author
authortext = author.text


@app.route('/')
def home():
    return render_template('home.html', quotetext=quotetext, authortext=authortext)


if __name__ == '__main__':
    app.run(debug=True)
