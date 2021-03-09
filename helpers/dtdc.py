from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium.common.exceptions import TimeoutException

def fetch_details_from_dtdc(id, type_):
    c_options = Options()
    c_options.add_argument('--headless')
    driver = webdriver.chrome.webdriver.WebDriver(
        'D:\Package_Status\parcel_feature_dtdc\parcel'
        '\drivers\windows\chromedriver.exe',
        options=c_options
    )
    driver.get('https://www.dtdc.in/tracking/shipment-tracking.asp')
    type_radio = driver.find_elements_by_id('TrkType2')
    
    for each_type in type_radio:
        if type_ == 'AWB/Consignment Number':
            if each_type.get_attribute('value') == 'awb_no':
                each_type.click()
                print('awb_no')

        elif type_ == 'Reference Number':
            if each_type.get_attribute('value') == 'ref_no':
                each_type.click()
                print('ref_no')
    
    text_area_number = driver.find_element_by_name('strCnno2')
    text_area_number.send_keys(id)
    track_button = driver.find_element_by_class_name('submit-button')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-button')))
    track_button.click()
    
    try:
        WebDriverWait(driver, 5).until (EC.alert_is_present())
        alert = driver.switch_to.alert
        return alert.text
    except TimeoutException:
        pass

    driver.implicitly_wait(3)
    html = BeautifulSoup(driver.page_source, features="html.parser")
    iframes  = html.find_all('iframe')[0]
    response = urlopen(iframes.attrs['src'])
    iframe_soup = BeautifulSoup(response,  features="html.parser")
    status = iframe_soup.find('td', {'id': 'lsSt'}).text.strip().split('\n')[0]
    driver.close()
    return status            
    



