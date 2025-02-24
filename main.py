from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException
import json


def launchBrowser(journal, article):
    driver = webdriver.Chrome()

    URL = f'https://periodicos.ufpe.br/revistas/index.php/{journal}/article/view/{article}'
    
    result = ""

    driver.get(URL)

    driver.implicitly_wait(3)
    
    try:
        pdf_link = driver.find_element(By.CSS_SELECTOR, 'a.obj_galley_link.pdf')
        pdf_link.click()
        driver.switch_to.frame(0)
        error_wrapper = driver.find_element(By.ID, "errorShowMore")
        try:
            error_wrapper.click()
            result += f"PDF AUSENTE EM {article} DE {journal}!!!! {URL}\n"
            #print(f"PDF AUSENTE EM {article} DE {journal}!!!!")
        except (ElementClickInterceptedException, ElementNotInteractableException) as e:
            #print(f"Não foi encontrada ausência de PDF em {article} de {journal}")
            result += f"Não foi encontrada ausência de PDF em {article} de {journal}\n"
    except (NoSuchElementException) as e:
        #print(f"Não foi encontrada ausência de PDF em: {article} de {journal}")
        result += f"Não foi encontrada ausência de PDF em {article} de {journal}\n"
    
    driver.quit()
    return result


with open('./data/data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

output = ""

for obj in data:
    output += launchBrowser(obj['journal'], obj['article'])

print(output)

with open('./data/output.txt', 'w', encoding='utf-8') as file:
    file.write(output)


