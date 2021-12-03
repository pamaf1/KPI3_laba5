from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def testSobike():
    searchText = 'bike'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(20)

    driver.get('https://sobike.com.ua/')
    driver.find_elements_by_css_selector('#search_term')[0].send_keys(searchText)
    driver.find_elements_by_css_selector('#search_term')[0].send_keys(Keys.ENTER)

    receivedText = driver.find_elements_by_css_selector('.cs-search-result-info__term')[0].text.lower()

    print(receivedText)
    assert receivedText == searchText, 'Error test'

    # python -m pytest test.py 