from selenium.webdriver.common.by import By

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver

       
        self.product_image = (By.XPATH, "//img[contains(@class, 'image-gallery-image')]")  
        self.product_name = (By.XPATH, "//h2[contains(@class, 'chakra-heading')]")  
        self.product_description = (By.XPATH, "//div[contains(@class, 'chakra-card__body')]/p[contains(text(), 'Description')]")  
        self.product_price = (By.XPATH, "//div[contains(@class, 'chakra-card__body')]/p[contains(text(), '$')]")  
        self.login_button = (By.XPATH, "//a[@href='/signin']") 
        self.register_button = (By.XPATH, "//a[@href='/signup']") 
        self.add_to_bag_button = (By.XPATH, "//button[contains(text(), 'Add to Cart') or contains(text(), 'Add to Bag')]")  

  
    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()


    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

 
    def click_add_to_bag_button(self):
        self.driver.find_element(*self.add_to_bag_button).click()

 
    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text

   
    def get_product_description(self):
        return self.driver.find_element(*self.product_description).text

   
    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text  