# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# # from selenium.webdriver.common.by import By
# # browser = webdriver.Chrome(ChromeDriverManager().install())
# # browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
#
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# caps = options.to_capabilities()
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
# # table = browser.find_element_by_xpath('//*[@id="Data_table"]')
# table = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]')
# table_text = table.text
# print(table_text)
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
# table = browser.find_element_by_xpath('by=By.XPATH, value=xpath')
table = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]')
table_text = table.text
lista = table_text.split('\n')
# print(lista)
header_len = browser.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}
# print(dictionar)
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        print(lista[i])
        dictionar[header[int(j)]].append(lista[i])
# print(header)
# print(table_text)
print(dictionar)
df = pd.DataFrame(dictionar)
df.to_csv("BNR_ALL_DATA.xls")
