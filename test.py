from time import sleep

from selenium import webdriver


class Test():

    def setup(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost/index.php")
        self.driver = driver

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test(self):
        self.driver.find_element_by_class_name("ecsc-search-input").send_keys("nishizhuma")
