from selenium import webdriver

class Homepage:

    link_customerRegistration_xpath = "//a[@class='ico-register']"
    link_customerRegistration_xpath = "//a[@class='ico-register']"
    link_customerLogin_xpath = "//a[@class='ico-login']"
    link_Wishlist_xpath = "//span[@class='wishlist-label']"
    link_shoppingcart_xpath = "//span[@class='cart-label']"
    searchbox_xpath = "//input[@id='small-searchterms']"
    searchbutton_xpath = "//button[@type='submit']"
    link_computers_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']"
    link_desktopcomputers_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Desktops']"
    link_notebookcomputers_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Notebooks']"
    link_softwarecomputers_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Software']"
    link_electronics_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']"
    link_cameraandphotoelectronics_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Camera & photo']"
    link_cellphoneselectronics_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Cell phones']"
    link_otherelectronics_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Others']"
    link_apparels_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Apparel']"
    link_shoeapparel_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Shoes']"
    link_clothingapparel_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Clothing']"
    link_accesorriesapparel_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Accessories']"
    link_digitaldownloads_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Digital downloads']"
    link_books_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Books']"
    link_jewellary_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Jewelry']"
    link_Giftcards_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Gift Cards']"


    def __init__(self, driver):
        self.driver = driver

    def loginlink(self):
        self.driver.find_element_by_xpath(self.link_customerLogin_xpath).click()

    def Registrationlink(self):
        self.driver.find_element_by_xpath(self.link_customerRegistration_xpath).click()

    def wishlistlink(self):
        self.driver.find_element_by_xpath(self.link_Wishlist_xpath).click()

    def shoppingcartlink(self):
        self.driver.find_element_by_xpath(self.link_shoppingcart_xpath).click()

    def searchbox(self, product):
        self.driver.find_element_by_xpath(self.searchbox_xpath).send_keys(product)

    def clicksearch(self):
        self.driver.find_element_by_xpath(self.searchbutton_xpath).click()


