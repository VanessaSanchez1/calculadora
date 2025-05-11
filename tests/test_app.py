import unittest
from app import app

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.post('/calculate', data={'num1': '2', 'num2': '3', 'operation': 'add'})
        self.assertIn("Resultado: 5.0", response.get_data(as_text=True))

    def test_subtraction(self):
        response = self.app.post('/calculate', data={'num1': '5', 'num2': '3', 'operation': 'subtract'})
        self.assertIn("Resultado: 2.0", response.get_data(as_text=True))

    def test_multiplication(self):
        response = self.app.post('/calculate', data={'num1': '2', 'num2': '3', 'operation': 'multiply'})
        self.assertIn("Resultado: 6.0", response.get_data(as_text=True))

    def test_division(self):
        response = self.app.post('/calculate', data={'num1': '6', 'num2': '3', 'operation': 'divide'})
        self.assertIn("Resultado: 2.0", response.get_data(as_text=True))

    def test_zero_division(self):
        response = self.app.post('/calculate', data={'num1': '6', 'num2': '0', 'operation': 'divide'})
        self.assertIn("Error: División por cero", response.get_data(as_text=True))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)