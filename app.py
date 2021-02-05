from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# entrada = input("Pesquisar: ")
entrada = '6206' # rolamento
entrada = entrada.replace(' ', '')



driver = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install())
driver.get("https://www.google.com")

input_element = driver.find_element_by_name("q")
input_element.send_keys(entrada)
input_element.submit()
# #############################################


