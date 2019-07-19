from bs4 import BeautifulSoup
import requests

r = requests.get('http://www.quotationspage.com/random.php').content
soup = BeautifulSoup(r, 'lxml')
a = soup.find_all('dt', class_='quote')
print(a[0].getText())


