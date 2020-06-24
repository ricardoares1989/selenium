from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests import SearchTests


# Vmamos  acrear variables con los cuales estaremos cargando los casos de prueba.
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

# Vamos a construir la suite de pruebas con codigo.
smoke_test = TestSuite([assertions_test, search_test])

# vamos a definir la forma de nuestro reporte.
kwargs = {
    'output': 'smoke-report'
}

# Pasamos los argumentos para generar el reporte como deseamos.
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)