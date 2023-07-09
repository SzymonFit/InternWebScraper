import requests
from bs4 import BeautifulSoup
import html.parser


url = "https://www.pracuj.pl/praca/krakow;wp?rd=0&cc=5015%2C5016&et=11"
url2 = "https://www.pracuj.pl/praca/programista;kw/krakow;wp?rd=0"
response = requests.get(url)
# web_page = response.text

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)





print(response.status_code)

# # selectors = {
# #     "value": ["div.data_test > input.listing_fhefgxl > value"]
# # }
# page = BeautifulSoup(response.text, 'html.parser')
# zmienna1 = page.select("div.listing_w1i46sjm")
# stos = zmienna1.pop(0)
# value = stos.select_one("#relative-wrapper > div.listing_w1i46sjm > div > div > div > div.listing_bvgive4 > div:nth-child(1) > div > div:nth-child(1) > div > input")
# print(value)