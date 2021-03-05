from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def fetch_details_from_bludart(waybill):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('/Users/h4xor/Desktop/github_proj/parcel/drivers/mac/chromedriver',
                              chrome_options=chrome_options)
    driver.get("https://www.bluedart.com/tracking")
    element = driver.find_element_by_id('trackingNo')
    element.send_keys(waybill)
    driver.find_element_by_id('goBtn').click()
    html = BeautifulSoup(driver.page_source, features="html.parser")
    status  = html.find("li", {"class": "list2 col-xs-8"})
    return status.text.strip().split(sep='\n')[1]