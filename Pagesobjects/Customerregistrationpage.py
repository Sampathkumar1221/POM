from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Registrationpage:

    radio_male_xpath = "//input[@id='gender-male']"
    radio_female_xpath = "//input[@id='gender-female']"
    textbox_firstname_xpath = "//input[@id='FirstName']"
    textbox_lastname_xpath = "//input[@id='LastName']"
    textbox_email_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    textbox_confirmpassword_xpath = "//input[@id='ConfirmPassword']"
    dropdown_day_xpath = "//select[@name='DateOfBirthDay']"
    dropdown_month_xpath = "//select[@name='DateOfBirthMonth']"
    dropdown_year_xpath = "//select[@name='DateOfBirthYear']"
    button_register_xpath = "//button[@id='register-button']"

    def __init__(self, driver):
        self.driver = driver


    def selectgender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_xpath(self.radio_male_xpath).click()
        elif gender == 'Female':
            self.driver.find_element_by_xpath(self.radio_female_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.radio_male_xpath).click()

    def enterfirstname(self, firstname):
        self.driver.find_element_by_xpath(self.textbox_firstname_xpath).send_keys(firstname)

    def enterlastname(self, lastname):
        self.driver.find_element_by_xpath(self.textbox_lastname_xpath).send_keys(lastname)

    def enteremail(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def enterpassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def confirmpassword(self, confirmpassword):
        self.driver.find_element_by_xpath(self.textbox_confirmpassword_xpath).send_keys(confirmpassword)

    def selectday(self, day):
        drop = Select(self.driver.find_element_by_xpath(self.dropdown_day_xpath))
        drop.select_by_visible_text(day)

    def selectmonth(self, month):
        drop2 = Select(self.driver.find_element_by_xpath(self.dropdown_month_xpath))
        drop2.select_by_visible_text(month)

    def selectyear(self, year):
        drop3 = Select(self.driver.find_element_by_xpath(self.dropdown_year_xpath))
        drop3.select_by_visible_text(year)

    def clickregister(self):
        self.driver.find_element_by_xpath(self.button_register_xpath).click()
    