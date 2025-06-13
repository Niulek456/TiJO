from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://localhost:5000")

# Sprawdzenie, czy nagłówek ma odpowiedni tekst
header = driver.find_element(By.TAG_NAME, "h1").text
assert header == "Rejestracja użytkownika"

print("✅ Test nagłówka zakończony pomyślnie.")
driver.quit()
