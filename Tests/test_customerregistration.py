import pytest
from Pagesobjects.Customerregistrationpage import Registrationpage
from Pagesobjects.Homepage import Homepage
from Utilities.Readproperties import Readconfig
from Utilities.customlogger import LogGen

class Test_001_customerregistration:

    baseURL = Readconfig.getApplicationurl()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_customerregisteration(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger = LogGen.loggen()
        self.crp = Registrationpage(self.driver)
        self.hp = Homepage(self.driver)
        self.hp.Registrationlink()
        self.logger.info("******* Starting customer registration Test **********")
        self.logger.info("************* Providing customer info **********")
        self.crp.selectgender('Male')
        self.crp.enterfirstname('sampath1994')
        self.crp.enterlastname('kumarrr')
        self.crp.enteremail('prashanthmca2010@gmail.com')
        self.crp.selectday('10')
        self.crp.selectmonth('May')
        self.crp.selectyear('1994')
        self.crp.enterpassword('samp666ath')
        self.crp.confirmpassword('samp666ath')
        self.crp.clickregister()
        self.msg = self.driver.find_element_by_xpath("//div[@class='result']").text


        if 'Your registration completed' in self.msg:
            assert True
            self.logger.info("********* customer registration Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Customerregistration_scr.png")  # Screenshot
            self.logger.error("********* customer registration Test Failed ************")
            assert False

        self.driver.close()


