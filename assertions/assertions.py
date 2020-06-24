import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# Nos servira como una excepcion para validar la presencia de un elemento.
from selenium.webdriver.common.by import By
# Nos ayudara a llamar las excepciones que queremos validar.

class AssertionsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'C:/Users/ricar/Documents/selenium/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://automationpractice.com/index.php')

    # Escribimos los metodos para nuestros assertions.
    # En este caso identificaremos la barra de busqeuda:
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME,'search_query')) 
    
    def test_cart_link(self):
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'shopping_cart'))

    def tearDown(self):
        self.driver.quit()

    # Pondremos una funcion para encontrar nuestros elementos
    # la funcion nos permitira identificar si un elemento esta presente de acuerdo a sus parametros
    # how nos identificara el tipo de selector, y what el valor que tiene.
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)     