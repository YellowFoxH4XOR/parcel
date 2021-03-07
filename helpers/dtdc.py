from selenium import webdriver
from bs4 import BeautifulSoup

def fetch_details_from_dtdc(id, type_):
    return {
        'type': type_,
        'id': id
    }