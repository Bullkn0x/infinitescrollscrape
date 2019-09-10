import time

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)

starttime = time.time()
try:
    SCROLL_PAUSE_TIME = .5
    driver.get("https://coinbase.com/prices")

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # driver.execute_script("window.scrollTo(0, 0.5*document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script("window.scrollTo(document.body.scrollHeight, document.body.scrollHeight-500);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            end= time.time()
            print(end-starttime)
            print('POSSIBLE END OF PAGE ---------------------')
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")
    print(soup)

    table= soup.find('tbody')
    print(table)
    coins = table.find_all('tr', class_='AssetTableRow__Wrapper-sc-1e35vph-0 hURHbs')

    for coin in coins:
        print(coin.find('h4', class_='Header__StyledHeader-sc-1q6y56a-0 eldbLX TextElement__Spacer-sc-18l8wi5-0 hpeTzd').text)


finally:
    driver.quit()