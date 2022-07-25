import requests
from bs4 import BeautifulSoup


baseurl = 'https://www.aliexpress.com/?spm=a2g0o.productlist.1000002.1.56924d70ZxRkAs'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

}

r = requests.get('https://www.aliexpress.com/category/100003084/hoodies-sweatshirts.html?trafficChannel=main&catName=hoodies-sweatshirts&CatId=100003084&ltype=wholesale&SortType=default&g=y&isrefine=y')

soup = BeautifulSoup(r.content, 'html.parser')

productlist  = soup.find_all('a', class_= '_3t7zg _2f4Ho')

print(productlist)