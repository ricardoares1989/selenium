import unittest
from pyunitreport import HTMLTestRunner
# Nos ayudara  a ejecutar las pruebas junto con los reportes.
from selenium import webdriver
# con ete nos comunicaremos con el navegador

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        # Para windows la ruta se indica con r'C://Users/ricar/Documents
        driver = cls.driver
        # nos evita escribir driver en cada linea.
        driver.implicitly_wait(10)
        # Esperara 10 segundos antes de realizar lo siguiente

    def test_hello_world(cls):
        driver = cls.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(cls):
        cls.driver.get('https://wwww.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # cerramos el driver.

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes',report_name='hello-world-report'))