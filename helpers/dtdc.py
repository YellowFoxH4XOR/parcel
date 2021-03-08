from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.request import urlopen

def fetch_details_from_dtdc(id, type_):
    c_options = Options()
    # options.add_argument('--headless')
    driver = webdriver.chrome.webdriver.WebDriver(
        'D:\Package_Status\parcel_feature_dtdc\parcel'
        '\drivers\windows\chromedriver.exe'
        # options=c_options
    )
    driver.get('https://www.dtdc.in/tracking/shipment-tracking.asp')
    type_radio = driver.find_elements_by_id('TrkType2')
    
    # for each_type in type_radio:
    #     if type_ == 'AWB/Consignment Number':
    #         if each_type.get_attribute('value') == 'awb_no':
    #             each_type.click()

    #     elif type_ == 'Reference Number':
    #         if each_type.get_attribute('value') == 'ref_no':
    #             each_type.click()
    
    text_area_number = driver.find_element_by_name('strCnno2')
    print(text_area_number)
    # text_area_number.click()
    text_area_number.send_keys(id)
    track_button = driver.find_element_by_class_name('submit-button')
    track_button.click()
    # WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.CLASS_NAME, '.widget-content')))
    driver.implicitly_wait(10)
    # .until(EC.visibility_of_element_located((By.ID, 'lsSt')))
    # status = driver.find_element_by_id('lsSt')
    # tab = driver.find_elements_by_class_name("table")
    # print(tab)
    # print(status)

    html = BeautifulSoup(driver.page_source, features="html.parser")
    status  = html.find_all('iframe')[0]
    print(status)
    response = urlopen(status.attrs['src'])
    iframe_soup = BeautifulSoup(response,  features="html.parser")
    print('*' * 50)
    print(iframe_soup)
                
    



