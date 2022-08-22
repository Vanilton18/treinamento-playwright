import unittest
from playwright.sync_api import sync_playwright
from page_object.models.user import UserPage

class UserTest(unittest.TestCase):


    def setUp(self) -> None:
        self.browser = sync_playwright().start().chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()


    def test_cadastro_usuario_valido(self):
        self.user_page = UserPage(self.page)
        self.user_page.acessar()
        self.user_page.abrir_tela_novo_usuario()
        user = {'login': 'mario_bobo', 'nome': 'Mario Santos', 'email': 'mario.santos@fpf.br', 'senha': '123456'}
        self.user_page.criar_novo_usuario(user)
        assert self.user_page.verificar_usuario_na_tabela('mario')


    def test_remover_usuario(self):
        pass


    def tearDown(self) -> None:
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
