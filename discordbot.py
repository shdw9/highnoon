from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

def check_exists_by_xpath(xpath):
	try:
		driver.find_element_by_xpath(xpath)
	except NoSuchElementException:
		return False
	return True


driver = webdriver.Chrome()

async def collect(username, password):
	channel = bot.get_channel(DISCORDCHANNELID)
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
		await channel.send("Collected points for " +  username + "! :white_check_mark: ")

		points = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div')
		print(username + " - " + points.text + " points")

		avatar = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/a[2]/img').get_attribute('src')

		embed=discord.Embed(title="playfull.com - " + username, url="https://playfull.com/", description=username + " has a total of " + points.text + " points :moneybag:", color=discord.Color.green())
		embed.set_thumbnail(url=avatar)
		await channel.send(embed=embed)
	else:
		print(username + " - No earnings available!")


	logout_button = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/span')
	logout_button.click()
	if (check_exists_by_xpath('/html/body/div/div[3]/div/div[3]/div')):
		x_button = driver.find_element_by_xpath('/html/body/div/div[3]/div/div[3]/div')
		x_button.click()
		print(username + " - Logged out!")


i = 0;

@bot.event
async def on_ready():
	print("The bot is ready!")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='playfull.com points'))
	channel = bot.get_channel(DISCORDCHANNELID)
	await channel.send(':eyes: Now watching playfull.com points :eyes: ')
	while i <= 10:
		await collect("USERNAME1", "PASSWORD1")
		time.sleep(300) # 5min interval
		await collect("USERNAME2", "PASSWORD2")
		time.sleep(300)

bot.run('DISCORDBOTTOKEN')
