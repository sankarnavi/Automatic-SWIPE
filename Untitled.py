from selenium import webdriver
from time import sleep


class Tinder():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com/')
        sleep(3)
        btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        btn.click()
        base_window = self.driver.window_handles[0]
        popup_window = self.driver.switch_to_window(
            self.driver.window_handles[1])
        emailbtn = self.driver.find_element_by_xpath(
            '//*[@id = "identifierId"]')
        emailbtn.send_keys('ssankar5627@gmail.com')
        sleep(3)
        next = self.driver.find_element_by_xpath(
            '// *[@id="identifierNext"]/span/span')
        next.click()
        sleep(3)
        password = self.driver.find_element_by_xpath(
            '// *[@id="password"]/div[1]/div/div[1]/input')
        password.send_keys('jackKUmar98@@~')
        next2 = self.driver.find_element_by_xpath(
            '//*[@id="passwordNext"]/span/span')
        sleep(10)
        next2.click()

        self.driver.switch_to_window(self.driver.window_handles[0])
        Mobile = self.driver.find_element_by_xpath(
            '// *[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        Mobile = self.driver.find_element_by_xpath(
            '// *[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        Mobile.send_keys('9486301446')
        Mobileclick = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[1]/button')
        Mobileclick.click()
        sleep(5)
        verify = self.driver.find_element_by_xpath(
            '//*[@id = "modal-manager"]/div/div/div[1]/button')
        verify.click()
        sleep(5)
        base_window = self.driver.window_handles[0]

        popup_window = self.driver.switch_to_window(
            self.driver.window_handles[1])

    def dislike(self):
        dislike = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike.click()

    def superlike(self):
        superlike = self.driver.find_element_by_xpath(
            '//*[@id = "content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[3]/div/div/div/button')
        superlike.click()

    def like(self):
        like = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like.click()


a = Tinder()
a.login()
sleep(30)
a.like()
