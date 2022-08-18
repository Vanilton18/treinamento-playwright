from playwright.sync_api import sync_playwright


def exemplo_de_navegacao():
    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    print("Acessado -> " + page.title())
    page.goto("https://bing.com")
    print("Acessado -> " + page.title())
    print("Atualizando página")
    page.reload()
    print("Retornando ao google")
    page.go_back()
    print("Avançando ao bing")
    page.go_forward()
    print("Acessado -> " + page.title())

def exemplo_de_interacao_captura():
    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    # Preencher campo de pesquisa (Seletor padrão CSS)
    #Mesmo exemplo com Xpath
    #page.locator('xpath=//input[@name="q"]')
    page.locator('[name="q"]').fill("Vanilton Pinheiro")
    # Capturar informações da página
    print(page.title())
    print(page.inner_html('html'))
    print("valor? -> " + page.locator('[name="q"]').input_value())
    print("oculto? -> " + page.locator('[name="q"]').is_hidden().__str__())
    print("visível? -> " + page.locator('[name="q"]').is_visible().__str__())
    print("disponível? -> " + page.locator('[name="q"]').is_enabled().__str__())
    print("Valor Atributo Aria Label? -> " + page.locator('[name="q"]').get_attribute("aria-label"))
    # Fechar página
    page.close()

def exemplo_circulo_visivel():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto("http://vanilton.net/web-test/display/")
    #made in Vanilton, Raphael
    print(page.locator('#circle').get_attribute("display"))
    #page.locator('.circle:visible').click()
    #page.locator('.circle >> visible=true').click()
    #page.locator('id=circle-clone').click()
    page.locator("#circle-clone").click()
    page.locator('#refresh-page').click()
    #page.locator('[onclick="AtualizarPagina()"]')
    page.locator("section", has=page.locator(".circle >> visible=true")).click()
    #print(page.locator("section:has(div.circle)").inner_text())
    #print(page.locator('section:has(button#refresh-page)').inner_text())

    sections = page.locator("section")
    for i in range(sections.count()):
        print(sections.nth(i).inner_text())
    #print(sections.all_inner_texts())
    # por índice
    #print(sections.all_inner_texts()[1])
    #sections.nth(1).inner_text()
    #print(sections.locator("h4", has_text="Op").inner_text())


    page.locator('button:has-text("Show Hide Elements"), button:has-text("Exibir Elementos Ocultos")').click()
    print(page.locator('#show-element').inner_text())
    page.locator('button:has-text("Show Hide Elements"), button:has-text("Exibir Elementos Ocultos")').click()
    print(page.locator('#show-element').inner_text())


def exemplos_xpath():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto("http://vanilton.net/web-test/display/")
    print("Inner do HTML " + page.locator("xpath=/html").inner_text())
    print("Inner do h4 " + page.locator("xpath=//h4").all_inner_texts().__str__())
    print("Inner do parent h4 " + page.locator("xpath=//h4/..").all_inner_texts().__str__())
    print("Inner de @style elements " + page.locator("xpath=//@style").all_inner_texts().__str__())


def exemplos_xpath_pedricados():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto("http://vanilton.net/web-test/display/")
    print("SECTION 1", page.locator("xpath=//section[1]").inner_text())
    print("SECTION LAST", page.locator("xpath=//section[last()]").inner_text())
    print("SECTION LAST -1 ", page.locator("xpath=//section[last()-1]").inner_text())
    print("CLASS ROUNDED", page.locator("xpath=//div[@class='rounded']").inner_text())
    print("SECTION / ELEMENTS > 3", page.locator("xpath=//section/*[position() >3]").all_inner_texts())
    print("ONCLICK FUNCTION", page.locator("xpath=//*[@onclick]").inner_text())


def exemplos_xpath_functions():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("http://vanilton.net/web-test/display/")
    print(page.locator("xpath=//button[contains(.,'Exibir')]").all_inner_texts())
    print(page.locator("xpath=//button[contains(.,'Exibir')] | //button[contains(.,'Hide')]").all_inner_texts())
    print(page.locator("xpath=//button[text()='Show Hide Elements']").all_inner_texts())
    print(page.locator("xpath=//button[@id and @onclick]").inner_text())
    print(page.locator('xpath=//div[contains(@id, "clone")]').get_attribute("id"))


def exemploeditar_pessoa():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("https://vanilton18.github.io/crud-local-storage-angular/")
    page.locator('id=nome').fill("Vanilton de Souza Freire Pinheiro")
    page.locator('[placeholder="Digite um email"]').fill("vanilton18@gmail.com")
    url_foto = "https://i.pinimg.com/originals/e4/34/2a/e4342a4e0e968344b75cf50cf1936c09.jpg"
    page.locator('[name=photo]').fill(url_foto)
    page.locator('text=Save').click()
    print(page.locator('xpath=//div[@class="card-block" and contains(.,"Vanilton")]').inner_text())
    # com xpath
    page.locator('xpath=//div[@class="card-block" and contains(.,"Vanilton")]//button[contains(.,"Editar")]').click()
    # com css
    #page.locator("css=div.card:has-text('Vanilton') >> css=button >> text=Edit").click()
    page.locator('id=nome').fill("Vanilton de S.F. Pinheiro")
    page.locator('[placeholder="Digite um email"]').fill("vanilton18@hotmail.com")
    page.locator('text=Save').click()
    print(page.locator('xpath=//div[@class="card-block" and contains(.,"Vanilton")]').inner_text())
    #print(page.locator('id=toast-container', has_text='Edição efetuada com sucesso!').is_visible())
    print(page.locator('[aria-label="Edição efetuada com sucesso!"]').is_visible())

def handle_dialog(dialog):
    print(dialog.message)


def exemplo_remover_pessoa_cadastrada():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("https://vanilton18.github.io/crud-local-storage-angular/")
    page.locator('id=nome').fill("Vanilton de Souza Freire Pinheiro")
    page.locator('[placeholder="Digite um email"]').fill("vanilton18@gmail.com")
    url_foto = "https://i.pinimg.com/originals/e4/34/2a/e4342a4e0e968344b75cf50cf1936c09.jpg"
    page.locator('[name=photo]').fill(url_foto)
    page.locator('text=Save').click()
    print(page.locator('xpath=//div[@class="card-block" and contains(.,"Vanilton")]').inner_text())
    page.locator('xpath=//div[@class="card-block" and contains(.,"Vanilton")]//button[contains(.,"Remover")]').scroll_into_view_if_needed()
    remove = page.locator("css=div.card:has-text('Vanilton') >> css=button >> text=Remover")
    page.on("dialog", lambda dialog: dialog.accept()) #Evento de captura do dialog
    page.on("dialog", handle_dialog)
    remove.click()
    print(page.locator("xpath=//div[@class='row']").inner_text() == '')


def exemplo_shadow_dom_acesso():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("http://vanilton.net/web-test/shadow-dom/")
    #print(page.locator('xpath=//fancy-tabs').locator('#nome').get_attribute("placeholder"))
    print(page.locator(':light(#nome)').get_attribute("placeholder"))


def exemplo_layout_locator():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("http://vanilton.net/web-test/shadow-dom/")
    print(page.locator("button:right-of(:text('Tab 2'))").first.inner_text())
    print(page.locator("button:left-of(:text('Tab 2'))").first.inner_text())
    #print(page.locator("button:left-of(:text('Tab 2'))").inner_text())
    #print(page.locator("button:right-of(:text('Tab 2'))").inner_text())
    print(page.locator(":above(:text('Tab 2'))").count())
    print(page.locator(":below(:text('Tab 2'))").count())
    print(page.locator("button:near(:text('Tab 2'))").all_inner_texts())


def exemplo_calculadora_raiz_quadrada():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("http://vanilton.net/calculatorSoapPHP/")
    #page.locator('input[name=num1] >> nth=1').fill("4")
    #page.locator('text="Resultado" >> nth=1').click()
    page.locator('[name="num1"] >> nth=1').fill('10')
    page.locator('text="Resultado" >> nth=-1').click()
    print(page.locator('html').inner_text())

def exemplo_calculadora_soma():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("http://vanilton.net/calculatorSoapPHP/")
    page.locator("input >> nth=0").fill('300')
    page.locator("input >> nth=1").fill('100')
    print(page.locator("input >> nth=0").input_value())
    page.locator("input[value='Resultado'] >> nth=0").click()
    print(page.locator('html').inner_text())


def exemplo_calculadora_divisao():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("http://vanilton.net/calculatorSoapPHP/")
    page.locator("input >> nth=0").fill('300')
    page.select_option('xpath=//select/option[contains(@value,"sum")]/..', value="div")
    page.locator("input >> nth=1").fill('100')
    print(page.locator("input >> nth=0").input_value())
    page.locator("input[value='Resultado'] >> nth=0").click()
    print(page.locator('html').inner_text())


def exemplo_calculadora_multiplicacao():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("http://vanilton.net/calculatorSoapPHP/")
    page.locator("input >> nth=0").fill('300')
    page.locator("input >> nth=0").fill('500')
    select = page.locator('select:has-text("*")')
    select.select_option(label="*")
    page.locator("input >> nth=1").fill('100')
    print(page.locator("input >> nth=0").input_value())
    page.locator("input[value='Resultado'] >> nth=0").click()
    print(page.locator('html').inner_text())


def exemplo_calculadora_subtracao():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("http://vanilton.net/calculatorSoapPHP/")
    page.locator("input >> nth=0").fill('300')
    page.select_option('select:has-text("*")', index=1)
    page.locator("input >> nth=1").fill('100')
    print(page.locator("input >> nth=0").input_value())
    page.locator("input[value='Resultado'] >> nth=0").click()
    print(page.locator('html').inner_text())



if __name__ == '__main__':
   #exemplo_de_interacao_captura()
   #exemplo_circulo_visivel()
   #exemplos_xpath()
   #exemplos_xpath_pedricados()
   #exemplos_xpath_functions()
   #exemploeditar_pessoa()
   #exemplo_remover_pessoa_cadastrada()
   #exemplo_shadow_dom_acesso()
   #exemplo_layout_locator()
   #exemplo_calculadora_subtracao()
   #exemplo_calculadora_multiplicacao()
   exemplo_upload()
   #exemplo_multiple_upload()