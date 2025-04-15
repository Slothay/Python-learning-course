from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# ------------- GET ADDRESSES -------------

address_list = []
address = soup.find_all('div', attrs={'class':"StyledPropertyCardDataWrapper"})
for div in address:
    adds = div.find_all('address')
    for add in adds:
        text = (add.getText()).strip().replace('|', '')
        address_list.append(text)

# ------------- GET PRICES -------------


price_list = []
price_data = soup.find_all('div', attrs={'class':"PropertyCardWrapper"})
for div in price_data:
    prices = div.find_all('span')
    for price in prices:
        text = price.getText().split('/', 1)[0]
        text = text.split('+',1)[0]
        price_list.append(text)


# ------------- GET LINKS -------------

link_list = []
link_data = soup.find_all('div', attrs={'class':"StyledPropertyCardDataWrapper"})
for div in link_data:
    links = div.find_all('a')
    for link in links:
        link_list.append(link.get('href'))

# ------------- FILL GOOGLE FORM -------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("GOOGLEFORMSADDRESS")

driver.maximize_window()

for i in range(0, len(address_list)-1):
    address_input = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    time.sleep(1)
    address_input.send_keys(address_list[i])
    price_input.send_keys(price_list[i])
    link_input.send_keys(link_list[i], Keys.ENTER)

    send = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    send.click()
    time.sleep(1)
    return_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    return_button.click()

driver.close()