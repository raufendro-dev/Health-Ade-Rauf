# Import the library Selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Make browser open in background
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Create the webdriver object
browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)

# Obtain the Google Map URL
link = "https://www.google.co.id/maps/search/rumah+sakit+diy/@-7.7869087,110.334042,14z"

# Open the Google Map URL
browser.get(link)

# Obtain the title of that place
title = browser.find_elements(By.CLASS_NAME, "hfpxzc")
get_nomor = browser.find_elements(By.XPATH, "//span[@jstcache='148']")
url = []
nama = []
nomor = []
list_nomor = [
	"(0274)",
	"0811-",
	"0812-",
	"0813-",
	"0814-",
	"0815-",
	"0816-",
	"0817-",
	"0818-",
	"0819-",
	"0821-",
	"0822-",
	"0852-",
	"0853-",
	"0823-",
	"0851-",
	"0855-",
	"0856-",
	"0857-",
	"0858-",
	"0859-",
	"0877-",
	"0878-",
	"0831-",
	"0832-",
	"0833-",
	"0838-",
	"0895-",
	"0896-",
	"0897-",
	"0898-",
	"0899-",
	"0881-",
	"0882-",
	"0883-",
	"0884-",
	"0885-",
	"0886-",
	"0887-",
	"0888-",
	"0889-",
	"0828-",
]

for x in title:
	url.append(x.get_attribute("href"))
	nama.append(x.get_attribute("aria-label"))

for y in get_nomor:
	for ln in list_nomor:
		if ln in y.text:
			nomor.append(y.text)

print(url)
print(nama)
print(nomor)