import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.meesho.com/w19pn"
response = requests.get(url)
html_code = BeautifulSoup(response.content, 'html.parser')

product_list = []

for product in html_code.find_all('div', class_='products'):
    # Parse the HTML code using BeautifulSoup
    soup = BeautifulSoup(product, 'html.parser')

    # Find the product details within the specified HTML structure
    product_container = soup.find('div', class_='NewProductCardstyled__CardStyled-sc-6y2tys-0')

    # Extract product name
    product_name = product_container.find('p', class_='NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5').text.strip()

    # Extract product price
    product_price = int(product_container.find('h5', class_='sc-iBYQkv hMaXQw').text.strip('₹').split()[0])

    # Extract product URL
    product_url = product_container.find('a')['href']

    # Extract image URL
    image_url = product_container.find('img')['src']
    
    product_data = {
        'name': name,
        'price': price,
        'image_url': image_url,
        'product_url': product_url
    }
    product_list.append(product_data)

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(product_list)

# Save the DataFrame to an Excel file
excel_file = 'product_data.xlsx'
df.to_excel(excel_file, index=False)

print(f"Product data saved to '{excel_file}'")
