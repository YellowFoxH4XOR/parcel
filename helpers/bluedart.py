from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

def fetch_details_from_bludart(waybill):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('/Users/h4xor/Desktop/github_proj/parcel/drivers/mac/chromedriver',
                              chrome_options=chrome_options)
    driver.get("https://www.bluedart.com/tracking")
    element = driver.find_element_by_id('trackingNo')
    element.send_keys(waybill)
    driver.find_element_by_id('goBtn').click()
    time.sleep(5)
    try:
        if(driver.find_element_by_xpath('//*[@id="errorDetails"]/div')):
            return {"status": "No Record Found"}
    except Exception:
        html = BeautifulSoup(driver.page_source, features="html.parser")
        status  = html.find("li", {"class": "list2 col-xs-8"})
        status = status.text.strip().split(sep='\n')[1]
        fstring = f'//*[@id="AWB{waybill}"]/div/div[2]/div/div/ul/li[2]/a'
        driver.find_element_by_xpath(fstring).click()
        time.sleep(3)
        fstring = f'//*[@id="SCAN{waybill}"]/div/table/tbody'
        x = driver.find_element_by_xpath(fstring)
        x = x.text
        scan_dets = x.strip().split(sep='\n')
        final = dict()
        final['status'] = status
        final['scan_details'] = scan_dets[:-1]
        return final