from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://fss.com.vn/spdv/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "pro-cell-1-3 pro-tab-cell-1-2 pro-mobile-cell-1-1 pro-pad-cell-1-3"})

filename = "products.csv"
with open(filename, "w", encoding="utf-8") as f:
    headers = "Product_Name\n"
    f.write(headers)

    for container in containers:
        a_tag = container.find("a")
        if a_tag:
            img_tag = a_tag.find("img")
            if img_tag and "alt" in img_tag.attrs:
                product_name = img_tag["alt"]
                print("Product_Name: " + product_name)
                f.write(product_name + "\n")
