import requests
from bs4 import BeautifulSoup

def get_trending_products(url="https://www.amazon.in/gp/bestsellers/"):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    products = []
    for item in soup.select('.p13n-sc-truncate-desktop-type2'):
        title = item.get_text(strip=True)
        if title:
            products.append(title)
        if len(products) == 5:
            break
    return products

if __name__ == "__main__":
    trending = get_trending_products()
    print("Trending Products:")
    for product in trending:
        print("-", product)