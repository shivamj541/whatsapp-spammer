from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com')

input(" Scan QR code and press ENTER...")

name = input("👤 Enter contact or group name: ")
message = input("💬 Enter message to send: ")
count = int(input("🔁 How many times: "))
delay = float(input("⏱️ Delay (seconds) between messages: "))
add_counter = input("🤖 Add counter (Y/N)? ").upper()

wait = WebDriverWait(driver, 30)
search_box = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
search_box.click()
search_box.clear()
search_box.send_keys(name)
time.sleep(2)

contact = wait.until(EC.presence_of_element_located(
    (By.XPATH, f'//span[@title="{name}"]')))
contact.click()

msg_box = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//footer//div[@contenteditable="true" and @data-tab]')))

for i in range(count):
    final_msg = f"<{i+1}/{count}> {message}" if add_counter == 'Y' else message
    msg_box.send_keys(final_msg + Keys.ENTER)
    time.sleep(delay)

msg_box.send_keys("✅ Done" + Keys.ENTER)
print("✅ Message sent successfully.")
time.sleep(5)
driver.quit()

