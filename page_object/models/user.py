class UserPage:

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto("http://lojafake.vanilton.net/#/usuarios")

    def abrir_tela_novo_usuario(self):
        self.page.locator('button', has_text='Novo Usuário').click()

    def criar_novo_usuario(self, user):
        self.page.locator('mat-card:has-text("Novo") >> input >> nth=0').fill(user.get('login'))
        self.page.locator('mat-card:has-text("Novo") >> input >> nth=1').fill(user.get('nome'))
        self.page.locator('mat-card:has-text("Novo") >> input >> nth=2').fill(user.get('email'))
        self.page.locator('mat-card:has-text("Novo") >> input >> nth=3').fill(user.get('senha'))
        self.page.locator('button:has-text("Salvar")').click()

    def verificar_usuario_na_tabela(self, atributo):
        self.page.set_default_timeout(3000)
        self.page.wait_for_selector("tr:has-text('"+atributo+"')")
        return self.page.locator('table >> tr', has_text=atributo).is_visible()

    def remove_usuario(self, nome):
        pass