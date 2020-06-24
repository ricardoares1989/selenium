import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# Nos servira como una excepcion para validar la presencia de un elemento.
from selenium.webdriver.common.by import By
# Nos ayudara a llamar las excepciones que queremos validar.

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:/Users/ricar/Documents/selenium/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://automationpractice.com/index.php')

    def test_search_dress(self):
        driver = self.driver
        search_field = driver.find_element_by_name('search_query')
        search_field.clear() #limpia en caso de que este lleno el campo
        search_field.send_keys('dress') # se simula la escritura
        search_field.submit() #envia los datos
        # Encontramos el elemento por xpath
        product = driver.find_elements_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img')
        self.assertEqual(1, len(product))

    def test_search_t_shirt(self):
        driver = self.driver
        search_field = driver.find_element_by_name('search_query')
        search_field.clear()
        search_field.send_keys('t-shirt')
        search_field.submit()




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)     