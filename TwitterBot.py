from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Safari()  #replace with the browser of your choice 

	def login(self):
		bot = self.bot
		bot.get('https://twitter.com/login')
		time.sleep(5)
		email = bot.find_element_by_class_name('email-input')
		password = bot.find_element_by_name('session[password]')
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(5)

	def like_tweet(self,hashtag):
		bot = self.bot
		bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
		time.sleep(5)
		for i in range(1,2):
			bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
			time.sleep(3)
			tweets = bot.find_element_by_class_name('tweet')
			links = [elem.get_attribute('data-permalink-patha') for elem in tweets]
			print(links)
		for link in links:
			bot.get('https://twitter.com'+link)
			try:
				bot.find_element_by_class_name('HeartAnimation').click()
				time.sleep(30)
			except:
				time.sleep(60)


a = TwitterBot('[enter your twitter username here, without brackets]', '[enter your twitter password here, without brackets]')
a.login()
tag = input("Enter the hashtag: ")
a.like_tweet(tag)