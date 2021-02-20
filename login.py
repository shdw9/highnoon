from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

def check_exists_by_xpath(xpath):
	try:
		driver.find_element_by_xpath(xpath)
	except NoSuchElementException:
		return False
	return True


driver = webdriver.Chrome()

def collect(username, password):
	driver.get("https://playfull.com/login")
	time.sleep(6)

	username_input = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div[2]/div[1]/div/input')
	username_input.send_keys(username)


	password_input = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div[2]/div[2]/div/input')
	password_input.send_keys(password)

	login_button = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div')
	login_button.click()
	print(username + " - Logged in!")
	time.sleep(5)

	if (check_exists_by_xpath('/html/body/div/div[3]/div/div[4]/div/div/div/span[1]')):
		time.sleep(3)
		print("Earnings available!")
		collect_button = driver.find_element_by_xpath('/html/body/div/div[3]/div/div[4]/div/div/div/span[1]')
		collect_button.click()
		print(username + " - Successfully collected earnings!")
	else:
		print(username + " - No earnings available!")

	points = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div')
	print(username + " - " + points.text + " points")

	logout_button = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/span')
	logout_button.click()
	if (check_exists_by_xpath('/html/body/div/div[3]/div/div[3]/div')):
		x_button = driver.find_element_by_xpath('/html/body/div/div[3]/div/div[3]/div')
		x_button.click()
		print(username + " - Logged out!")
	time.sleep(1) #seconds to loop each logout

i = 0;

while i <= 10:
	collect("USERNAME", "PASSWORD")
