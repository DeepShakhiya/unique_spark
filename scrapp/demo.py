from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://www.meesho.com/w19pn?page=6")
time.sleep(5)
all_elements = driver.find_elements(By.XPATH,'//*[@id="__next"]/div[3]/div/div[4]/div/div/div/div/div/div[3]/div[2]/div[2]/div/div')

# Define column names
columns = ['Name', 'Price', 'Image_link','Product_link']
df = pd.DataFrame(columns=columns)
for element in all_elements:

    time.sleep(2)
    product_link = element.find_element(By.TAG_NAME,"a").get_attribute('href')
    image_link = element.find_element(By.TAG_NAME,"img").get_attribute('src')
    name = element.find_element(By.TAG_NAME,"p")
    price = element.find_element(By.TAG_NAME,"h5")

    print("name: ",name.text)
    print("price: ",(price.text.split()[0]))
    print("image link: ",image_link)
    print("product_link: ",product_link)
    df.loc[len(df.index)]=(name.text, price.text.split()[0], image_link, product_link)
    print("#"*20)

time.sleep(2)
df.to_csv("data.csv")

driver.quit()
