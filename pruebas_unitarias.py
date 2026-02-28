import unittest
from contactos import GestorContactos, Contacto

class TestGestorContactos(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorContactos()
        self.contacto = Contacto("Juan", "123456", "juan@email.com", "Calle 1")
        self.gestor.agregar(self.contacto)
    
    def test_agregar(self):
        self.assertEqual(len(self.gestor.contactos), 1)
    
    def test_buscar(self):
        resultados = self.gestor.buscar("Juan")
        self.assertEqual(len(resultados), 1)
    
    def test_eliminar(self):
        self.gestor.eliminar(0)
        self.assertEqual(len(self.gestor.contactos), 0)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)
