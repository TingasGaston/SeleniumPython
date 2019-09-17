import unittest
from selenium import webdriver


class TwitterClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://twitter.com/")
        self.assertEqual(True, False)

    def login(self):
        self.user = self.driver.find_element_by_name("session[username_or_email]")
        self.user.send_keys("gastonarios@yahoo.com.ar")

        self.password = self.driver.find_element_by_name("session[password]")
        self.password.send_keys("")
        self.loginButton = self.driver.find_element_by_xpath(
            "/html/body[@class='three-col logged-out ms-windows static-logged-out-home-page no-nav-banners']/div[@id='doc']/div[@class='StaticLoggedOutHomePage']/div[@class='StaticLoggedOutHomePage-content']/div[@class='StaticLoggedOutHomePage-cell StaticLoggedOutHomePage-utilityBlock']/div[@class='StaticLoggedOutHomePage-login']/form[@class='LoginForm js-front-signin']/input[@class='EdgeButton EdgeButton--secondary EdgeButton--medium submit js-submit']")
        self.loginButton.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
