import pytest
from selenium import webdriver
from Pagesobjects.Customerloginpage import Loginpage
from Pagesobjects.Homepage import Homepage
from Utilities.Readproperties import Readconfig
from Utilities.customlogger import LogGen


class Test_loginpage:

    base_url = Readconfig.getApplicationurl()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.hp = Homepage(self.driver)
        self.lp = Loginpage(self.driver)
        self.hp.loginlink()
        self.lp.enteremail(self.username)
        self.lp.enterpassword(self.password)
        self.lp.clicklogin()
        logintitle = self.driver.title
        if logintitle == "nopCommerce demo store. Account":
            assert True
            self.logger.info('****************logintest passed******************')
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots" + "test_login.png")
            self.driver.close()
            self.logger.error('****************logintest failed******************')
            assert False

        self.driver.close()




