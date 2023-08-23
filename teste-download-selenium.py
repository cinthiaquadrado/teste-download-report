from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do navegador (neste exemplo, o Chrome é utilizado)
driver = webdriver.Chrome(executable_path='caminho_para_o_executavel_do_chrome')

# URL do site
base_url = 'https://exemplo.com/'

# Abrir o site
driver.get(base_url)

# Localizar e clicar no botão à direita
right_button = driver.find_element(By.ID, 'right-button-id')
right_button.click()

# Aguardar até que a janela pop-up seja carregada
popup_window = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'popup-id')))

# Clicar no botão de exportar
export_button = popup_window.find_element(By.ID, 'export-button-id')
export_button.click()

# Aguardar até que a janela de opções seja carregada
options_window = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'options-window-id')))

# Selecionar "Detalhes" nas opções
details_option = options_window.find_element(By.ID, 'details-option-id')
details_option.click()

# Selecionar "Formato Excel .xlsx"
excel_format_option = options_window.find_element(By.ID, 'excel-format-option-id')
excel_format_option.click()

# Clicar no botão de exportar novamente
export_button_again = options_window.find_element(By.ID, 'export-button-id')
export_button_again.click()

# Aguardar um curto período para o download ser iniciado
time.sleep(5)

# Fechar o navegador
driver.quit()
