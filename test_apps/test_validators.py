import unittest
import validators

'''
partição inválida ['1, _1, '',']
partição válida [a23, eer, AAA2]
análise do valor limite (limites) aaa, aa, a123456789, a1234567890
executa sempre a cada teste    
'''


class ValidatorsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp mãe')
        self.validator = validators.Validators


    def test_minimo_caracteres_valido(self):
        result = self.validator.check_valid_identifier(self, 'a23')
        self.assertTrue(result)


    def test_minimo_caracteres_invalido(self):
        result = self.validator.check_valid_identifier(self, 'a')
        self.assertFalse(result)


    def tearDown(self) -> None:
        print('tearDowm pai')
        self.validator = None


if __name__ == '__main__':
    unittest.main()
