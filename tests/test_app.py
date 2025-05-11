import unittest
from app import app

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.post('/calculate', data={'num1': '2', 'num2': '3', 'operation': 'Sumar'})
        self.assertIn(b'Resultado: 5.0', response.data)

    def test_subtraction(self):
        response = self.app.post('/calculate', data={'num1': '5', 'num2': '3', 'operation': 'resta'})
        self.assertIn(b'Resultado: 2.0', response.data)

    def test_multiplication(self):
        response = self.app.post('/calculate', data={'num1': '2', 'num2': '3', 'operation': 'multiplicacion'})
        self.assertIn(b'Resultado: 6.0', response.data)

    def test_division(self):
        response = self.app.post('/calculate', data={'num1': '6', 'num2': '3', 'operation': 'division'})
        self.assertIn(b'Resultado: 2.0', response.data)

    def test_zero_division(self):
        response = self.app.post('/calculate', data={'num1': '6', 'num2': '0', 'operation': 'division'})
        self.assertIn(b'Error: Division by zero', response.data)

if __name__ == '__main__':
    unittest.main()