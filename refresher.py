###refresher

import numpy
import scipy

import selenium



DRIVER_PATH = '/usr/local/bin/chromedriver'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('https://google.com')



### Generate headless browser
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://resy.com/cities/ny/gotham-ny?date=2022-07-26&seats=2/")
print(driver.page_source)
#driver.quit()


for request in driver.requests:
  print(request.url) # <--------------- Request url
  print(request.headers) # <----------- Request headers
  print(request.response.headers) # <-- Response headers


### HTML parser

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='modal-footer']//button[@Class='btn btn-danger x' and text()='Maybe Later']"))).click()

# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@Class='ReservationButton Button Button--primary']"))).click()

#<button class="ReservationButton Button Button--primary" type="button" id="rgs://resy/7104/1781796/2/2022-07-26/2022-07-26/19:30:00/2/Dining Room"><div class="ReservationButton__time">7:30PM</div><div class="ReservationButton__type">Dining Room</div></button>










