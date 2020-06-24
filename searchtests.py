import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.get('http://automationpractice.com/index.php')
        # pediremos que se maximice la ventana ya que el responsive puede cambiar la ubicacion u orden.
        driver.maximize_window()
        driver.implicitly_wait(15)

    # Vamos a encontrar un campo de texto
    # def test_search_text_field(self):
    #     # PAra identificar nuestro campo de busqueda lo vamos a asignar una variable.
    #     # debe hacer con comillas.
    #     search_field = self.driver.find_element_by_id('search_query_top')

    # def test_search_text_field_by_name(self):
    #     search_field = self.driver.find_element_by_name('search_query')

    # def test_search_text_field_by_class_name(self):
    #     search_field = self.driver.find_element_by_class_name('form-control')
    
    # def test_search_button_enabled(self):
    #     button = self.driver.find_element_by_class_name('button-search')

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_css_selector('ul.htmlcontent-home.clearfix.row')
        # Obtendremos el elemento que los contiene, y despues almacenaremos.
        banners = banner_list.find_elements_by_tag_name('img')
        # Vamos a contar los elementos img que hay dentro del elemento.
        self.assertEqual(2,len(banners))
        # Vamos a hacer un assertEqual para verificar que sean 2 imagenes, hara match en el primer elemento que encuentre
        # que cumpla con las caracteristicas.
    def test_promo_vip(self):
        via_promo = self.driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/a/img')


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)