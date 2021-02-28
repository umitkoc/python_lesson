from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Instagram:
    def __init__(self,username,password):
        path = 'chromedriver.exe'
        self.url ='https://www.instagram.com/'
        self.browser=webdriver.Chrome(path)
        self.browser.maximize_window()
        self.username=username
        self.about=open('instagram.txt','w',encoding='utf-8')
        self.password=password
        self.followers_data=[]
        self.follow_data=[]
        self.Open()
    def Open(self):
        self.browser.get(self.url)
        sleep(2)
        self.Login()
    def Login(self):
        self.browser.find_element_by_name('username').send_keys(self.username)
        self.browser.find_element_by_name('password').send_keys(self.password)
        sleep(1)
        self.browser.find_element_by_name('password').send_keys(Keys.ENTER)
        sleep(1)
        self.Page()
    def Page(self):
        try:
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
            sleep(2)
            self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        except:
            return self.Page()
        self.Profile()
    def Profile(self):
        self.browser.get(f'{self.url}{self.username}')
        self.Followers()
    def Followers(self):
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(2)
        count = int(self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text)
        modal = self.browser.find_element_by_css_selector('div[role=dialog] ul')
        i = len(modal.find_elements_by_tag_name('li'))
        action=webdriver.ActionChains(self.browser)
        while i<count:
            modal.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            sleep(2)
            newcount=len(modal.find_elements_by_tag_name('li'))
            if i!=newcount:
                i=newcount
            else:
                break

        followers = modal.find_elements_by_tag_name('li')
        self.about.write(f'Followers ({count}) \n')
        i=1
        for use in followers:
            link=use.find_element_by_tag_name('a').get_attribute('href')
            self.about.write(f'{i}: {link}\n')
            self.followers_data.append(link)
            i+=1
        self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
        self.Close()
        self.Follow()
    def Follow(self):
        sleep(3)
        count = int(self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text)
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(2)
        modal = self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul')
        i = len(modal.find_elements_by_tag_name('li'))
        action = webdriver.ActionChains(self.browser)
        while i < count:
            modal.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            sleep(2)
            newcount = len(modal.find_elements_by_tag_name('li'))
            if i != newcount:
                i = newcount
            else:
                break
        follow = modal.find_elements_by_tag_name('li')
        i=1
        self.about.write(f'FOLLOW ({count})\n')
        for use in follow:
            link=use.find_element_by_tag_name('a').get_attribute('href')
            self.about.write(f'{i}: {link}\n')
            self.follow_data.append(link)
            i+=1
        sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
        self.Close()
    def Close(self):
        self.browser.close()
        self.about.close()
        print('close...')
    








