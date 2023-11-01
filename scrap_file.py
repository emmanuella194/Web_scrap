
from bs4 import BeautifulSoup
import requests
url = "https://www.edusko.com/school/search?category=high_school&country=nigeria"


result = requests.get(url)
print(result.text)
