# anticaptcha ## pip install anticaptchaofficial


from anticaptchaofficial.recaptchav2proxyless import *
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = "https://www.google.com/recaptcha/api2/demo"
driver.get(url)

sitekey = driver.find_element(By.XPATH, "//*[@id='recaptcha-demo']").get_attribute('outerHTML')
print(sitekey)
sitekey_clean = sitekey.split('" data-callback')[0].split('data-sitekey="')[1]


anticaptcha_api_key = "ab62dd9dca139fc22606e1ca4beddcac"

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(anticaptcha_api_key)
solver.set_website_url(url)
solver.set_website_key(sitekey_clean)
print(sitekey_clean)

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print("g_response"+g_response)
else:
    print("task finished with error"+solver.error_code)

driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""",g_response)
driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')

driver.find_element(By.XPATH, '//*[@id="recaptcha-demo-submit"]').click()
time.sleep(2)