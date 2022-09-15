import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://www.naukri.com/data-analyst-jobs-in-india?k=data%20analyst&l=india&functionAreaIdGid=3').text#
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')