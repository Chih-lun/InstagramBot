from time import sleep
from selenium import webdriver
import random

class instagram_bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='C:\\Users\\Allen\\OneDrive\\桌面\\geckodriver')

    def login(self,username,userpassword):
        self.driver.get('https://www.instagram.com/')
        self.driver.implicitly_wait(10)

        the_username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        the_username.send_keys(username)
        the_userpassword = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        the_userpassword.send_keys(userpassword)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        sleep(5)

        # 安全碼
        try:
            secure_code = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div/label/input')
            if secure_code:
                the_secure_code = input('Please enter your secure code: ')
                secure_code.send_keys(the_secure_code)
                comfirm_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div[2]/button')
                comfirm_button.click()
        except:
            print('There is no secure code')

        skip_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        skip_button.click()
        notification_button = self.driver.find_element_by_class_name('aOOlW.HoLwm ')
        notification_button.click()
        sleep(6)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(10)

    #hashtag is a list
    def like_hashtag(self,hashtag):
        for h in hashtag:
            self.driver.get(f'https://www.instagram.com/explore/tags/{h}/')
            sleep(10)
            for i in range(0,3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(120)
            photo_hrefs = self.driver.find_elements_by_tag_name('a')
            links = []
            for h in photo_hrefs:
                the_herf = h.get_attribute('href')
                if 'https://www.instagram.com/p/' in the_herf:
                    links.append(the_herf)
            ran_links = random.sample(links,50//len(hashtag))
            random.shuffle(ran_links)
            print(ran_links)
            for l in ran_links:
                print(l)
                self.driver.get(l)
                sleep(30)
                like_button = self.driver.find_element_by_class_name('fr66n')
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                like_button.click()
                sleep(30)

