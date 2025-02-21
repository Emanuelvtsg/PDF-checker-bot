from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
import json


def launchBrowser(journal, article):
    driver = webdriver.Chrome()

    URL = f'https://periodicos.ufpe.br/revistas/index.php/{journal}/article/view/{article}'
    #URL = 'https://periodicos.ufpe.br/revistas/index.php/70/article/view/248782'
    
    print (URL)
    driver.get(URL)

    driver.implicitly_wait(3)

    pdf_link = driver.find_element(By.CSS_SELECTOR, 'a.obj_galley_link.pdf')

    pdf_link.click()

    driver.switch_to.frame(0)

    error_wrapper = driver.find_element(By.ID, "errorShowMore")

    try:
        error_wrapper.click()  # Try to click
        print(f"Success on article {article} of journal {journal}")
    except (ElementClickInterceptedException, ElementNotInteractableException) as e:
        print(f"!!ERROR!! ON ARTICLE {article} OF JOURNAL {journal}")

    while(True):
        pass

with open('data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

with open('output.txt', 'w', encoding="utf-8") as file:
    i = 0
    for obj in data:
        if i<1:
            print (obj['journal'])
            print (obj['article'])
            launchBrowser('clioarqueologica', '248782')
            i += 1

#launchBrowser('clioarqueologica', '248782')

