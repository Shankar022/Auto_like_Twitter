from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = bot.find_element_by_class_name("js-username-field")
        password =  bot.find_element_by_class_name("js-password-field")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        bot.implicitly_wait(1)
        password.send_keys(self.password)
        bot.implicitly_wait(1)
        bot.find_element_by_class_name("EdgeButtom--medium").click()
        bot.implicitly_wait(1)

    def like_tweet(self,hashtag):
        bot =  self.bot
        bot.get('https://twitter.com/search?q=' + hashtag +'&src=typd')
        time.sleep(3)
        for i in range(1,10):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            tweets = bot.find_elements_by_class_name("tweet")
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]

            print(links)
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name("HeartAnimation").click()
                    bot.implicitly_wait(1)
                except Exception as ex:
                    time.sleep(30)


ed = TwitterBot('your username /email','password')
ed.login()
ed.like_tweet('topic you want to like')