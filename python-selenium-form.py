from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://localhost:5000")

# Znajdź i wypełnij pola formularza
driver.find_element(By.NAME, "login").send_keys("jan123")
driver.find_element(By.NAME, "first_name").send_keys("Jan")
driver.find_element(By.NAME, "last_name").send_keys("Kowalski")
driver.find_element(By.NAME, "password").send_keys("Test123!")
driver.find_element(By.NAME, "pesel").send_keys("44051401458")

# Kliknij przycisk „Zapisz”
driver.find_element(By.TAG_NAME, "button").click()

# Poczekaj na rezultat (np. komunikat potwierdzający)
time.sleep(2)

# Weryfikacja – czy nie ma komunikatu o błędach
body = driver.find_element(By.TAG_NAME, "body").text
assert "Błąd" not in body

print("✅ Test formularza zakończony pomyślnie.")
driver.quit()
