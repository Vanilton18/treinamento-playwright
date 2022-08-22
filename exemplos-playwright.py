import base64
import json
import time

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


def exemplo_calculadora():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("http://vanilton.net/calculatorSoapPHP/")
    page.locator("input >> nth=0").type("2", delay=1000)
    select = page.locator('select:has-text("*")')
    select.select_option(label="*")
    page.locator("input >> nth=1").type("4", delay=1000)
    page.locator("input[value='Resultado'] >> nth=0").click()
    #resultado = page.locator('body').inner_text().split('\n')[0]
    resultado = page.evaluate('x = document.getElementsByTagName("body")[0]; x.firstChild.textContent')
    print(resultado)
    # Raiz Quadrada
    page.go_back()
    page.reload()
    page.locator('[name="num1"] >> nth=1').type("4", delay=1000)
    page.locator('text="Resultado" >> nth=-1').click()
    #resultado = page.locator('body').inner_text().split('\n')[0]
    resultado = page.evaluate('x = document.getElementsByTagName("body")[0]; x.firstChild.textContent')
    print(resultado)
    page.go_back()
    page.reload()
    # Coseno
    select = page.locator('select:has-text("Raiz")')
    select.select_option(label="Coseno")
    page.locator('[name="num1"] >> nth=1').type("5", delay=1000)
    page.locator('text="Resultado" >> nth=-1').click()
    #resultado = page.locator('body').inner_text().split('\n')[0]
    resultado = page.evaluate('x = document.getElementsByTagName("body")[0]; x.firstChild.textContent')
    print(resultado)

def exemplo_evaluate_screen_size():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("http://vanilton.net/web-test/promise/")
    # Cria o objeto window
    object_handle = page.evaluate_handle('window')
    print(object_handle.json_value())
    # Passando por parâmetro um handle e recuperando seu innerHTML
    body_handle = page.evaluate_handle('document.body')
    body_text = page.evaluate("body => body.innerHTML", body_handle)
    print(body_text)
    # Tamanho da tela
    width = page.evaluate_handle('window.screen.width')
    height = page.evaluate_handle('window.screen.height')
    print("Largura: {} - Altura: {}".format(width, height))
    # Encerra a referência ao elemento
    body_handle.dispose()
    object_handle.dispose()


def exemplo_element_handle():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto("http://vanilton.net/blog")
    href_element = page.query_selector("a")
    print(href_element.inner_text())


def exemplo_keyboard():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto("https://google.com")
    busca = page.locator('[name="q"]')
    busca.focus()
    page.keyboard.type("Hello World!", delay=500)
    page.keyboard.press("ArrowLeft")
    page.keyboard.down("Shift")  # down (segura a tecla)
    for i in range(6):
        page.keyboard.press("ArrowLeft", delay=1000)
    page.keyboard.up("Shift")  # up (solta a tecla)
    page.keyboard.press("Backspace")
    print(busca.input_value())

def exemplo_keyboard():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto("https://keycode.info")
    page.keyboard.type('Meta+a')
    print(page.locator('div.item-event').inner_text())
    page.screenshot(path='image/meu_primeiro_screenshot2.png', full_page=True)
    page.locator('div.item-event').screenshot(path='image/card-event2.png')


def print_request_sent(request):
    print("Request sent: " + request.url)

def print_request_finished(request):
    print("Request finished: " + request.url)

def print_request_response(request):
    print("Request response: " + request.url)

# Execute essa função e observe o console da IDE
def test_wait_add_remove_event_listener():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.on("request", print_request_sent)
    page.on("response", print_request_response)
    page.on("requestfinished", print_request_finished)
    page.remove_listener("requestfinished", print_request_finished)
    page.goto("https://ge.globo.com")
    page.goto("https://wikipedia.org")


def exemplo_evento_expect_request():
    page = sync_playwright().start().chromium.launch().new_page()
    #with page.expect_request("**/*teste*.png") as first:
    with page.expect_request("**teste_agil-520x389.png") as first:
        page.goto("http://vanilton.net/blog")
    print(first.is_done())
    print(first.value.headers)
    print(first.value.url)
    print(first.value.response())


def exemplo_iframe():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto("http://vanilton.net/web-test/iframe/")
    frame_element = page.frame_locator('[name=iframe_artigos]')
    print(frame_element.locator('title').inner_text())
    page.locator('text=Como ser um facilitador?').click()
    frame_element.locator('[id=page]').wait_for(timeout=10000)
    print(frame_element.locator('title').inner_text())


def exemplo_check_and_radio_buttons():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto("http://vanilton.net/web-test/input-types/")
    page.locator('id=M').check()
    print(page.locator('id=output').inner_text().__contains__('M') is True)
    page.locator('id=Bike').check()
    page.locator('id=Moto').check()
    print(page.locator('id=Moto').is_checked())
    print(page.locator('id=Bike').is_checked())
    print(page.locator('id=Barco').is_checked())
    print(page.locator('id=output-check').inner_text().__contains__('Bike' and 'Moto') is True)
    screen = page.screenshot()
    result = base64.b64encode(screen).decode();
    print(result)

def exemplo_save_images():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto('http://lojafake.vanilton.net')
    page.locator('img').first.wait_for(state='visible')
    page.screenshot(path='image/loja-fake.png', full_page=True)
    images = page.locator('img')
    for i in range(images.count()):
        nome = images.nth(i).get_attribute('name')
        images.nth(i).screenshot(path=f'images/{nome}.png')


#Resolve o problema de drag drop do angular
def drag_drop_custom(page, source, target):
    source.hover()
    page.mouse.down()
    print('Posição e tamanho do body: ' + page.locator('body').bounding_box().__str__())
    print('Posição e tamanho do source: ' + source.bounding_box().__str__())
    print('Posição e tamanho do target: ' + target.bounding_box().__str__())
    box = target.bounding_box()
    print('Movendo source para target em: ' + (box['x'] + box['width'] / 2, box['y'] + box['height'] / 2).__str__())
    # Mover para o centro do elemento relativo ao tamanho da página (x,y)
    page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2)
    target.hover()
    page.mouse.up()

def exemplo_loja_fake():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto("http://lojafake.vanilton.net/")
    page.locator("div:has-text(\"Usuário\")").nth(4).click()
    page.locator("#mat-input-0").fill("admin")
    page.locator("#mat-input-1").fill("1234")
    page.locator("button:has-text(\"Login\")").click()
    page.locator("text=Minhas Listas").click()
    page.wait_for_url("http://lojafake.vanilton.net/#/drag-drop")
    page.locator("text=Filmes").click()
    drag_drop_custom(page, page.locator("div:text('3 - O Poderoso Chefão II')"), page.locator("#cdk-drop-list-2"))
    page.wait_for_timeout(3000)
    print(page.locator("#cdk-drop-list-2").inner_text())

def exemplo_drag_drop_html5():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.goto("http://vanilton.net/web-test/drag-drop/")
    page.drag_and_drop("id=drag1", 'id=div2')
    print(page.locator("[id='content1']").inner_text())
    page.drag_and_drop("id=drag1", "id=div1")
    print(page.locator("[id='content2']").inner_text())


def exemplo_context_trace():
    browser = sync_playwright().start().chromium.launch(timeout=60000)
    context = browser.new_context()
    context.tracing.start(snapshots=True, screenshots=True, sources=True)
    page = context.new_page()
    page.goto("http://lojafake.vanilton.net/")
    page.locator("div:has-text(\"Usuário\")").nth(4).click()
    page.locator("#mat-input-0").fill("admin")
    page.locator("#mat-input-1").fill("1234")
    page.locator("button:has-text(\"Login\")").click()
    page.locator("text=Minhas Listas").click()
    page.wait_for_url("http://lojafake.vanilton.net/#/drag-drop")
    page.locator("text=Filmes").click()
    drag_drop_custom(page, page.locator("div:text('3 - O Poderoso Chefão II')"), page.locator("#cdk-drop-list-2"))
    page.wait_for_timeout(3000)
    print(page.locator("#cdk-drop-list-2").inner_text())
    context.tracing.stop(path='trace/trace_loja_fake.zip')
    browser.close()


def exemplo_confs():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context(
        viewport={'width': 1024, 'height': 720}
    )
    context.tracing.start(snapshots=True, screenshots=True, sources=True)
    page = context.new_page()
    #page.set_default_navigation_timeout(1000)
    page.goto('https://google.com')
    print('Site ta up')
    page.set_default_timeout(5000)
    page.locator('area-principal2').click()


def preenche_input(page, label, value):
    page.locator(f"//div[contains(.,'{label} *')]/input").fill()

def loja_fake_cadastro_usuario():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(snapshots=True, screenshots=True, sources=True)
    page = context.new_page()
    page.goto("http://lojafake.vanilton.net/#/usuarios")
    page.locator('button', has_text='Novo Usuário').click()
    page.locator('mat-card:has-text("Novo") >> input >> nth=0').fill('mario.mario')
    page.locator('mat-card:has-text("Novo") >> input >> nth=1').fill('Mario Mario')
    page.locator('mat-card:has-text("Novo") >> input >> nth=2').fill('mario.mario@mario.mario')
    page.locator('mat-card:has-text("Novo") >> input >> nth=3').fill('mario')
    page.locator('button:has-text("Salvar")').click()
    page.wait_for_selector('tr:has-text("mario")')
    print(page.locator('table >> tr', has_text='mario.mario').is_visible() == True)


def contexto_vida():
    browser = sync_playwright().start().chromium.launch(headless=False)
    #Criando dois contextos
    context = browser.new_context()
    context2 = browser.new_context()
    # Criar paginas para o contexto
    pagec1 = context.new_page()
    pagec1.pause()
    pagec1_1 = context.new_page()
    pagec2 = context2.new_page()
    pagec2_2 = context2.new_page()
    pagec1.goto("http://lojafake.vanilton.net/#/usuarios")
    pagec2.goto("https://fpftech.com")
    pagec2_2.goto('https://google.com')
    pagec1_1.goto('https://bing.com')


def context_propriedades():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context(
        geolocation={'longitude': 12.492348, 'latitude': 41.890221},
        permissions=['geolocation'],
        record_video_dir='video/',
        record_video_size={'width': 800, 'height': 600},
        timezone_id="Europe/Rome",
        locale="it-IT"
    )
    page = context.new_page()
    page.goto("https://maps.google.com")
    page.locator("button[aria-label='Mostra la tua posizione']").click()


def exemplo_input_file():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("https://google.com")
    page.screenshot(full_page=True, path='google.png')
    page.goto("http://vanilton.net/web-test/upload/")
    page.locator('input#fileToUpload').set_input_files('google.png')
    page.locator('[name=submit]').click()
    print(page.locator('a').get_attribute('href'))

def exemplo_multiple_upload():
    page = sync_playwright().start().chromium.launch(headless=False).new_page()
    page.set_default_timeout(5000)
    page.goto("https://google.com")
    page.goto('http://vanilton.net/web-test/upload/multiple')
    page.locator('id=filesToUpload').set_input_files(['google.png', 'meu_pdf_maroto.pdf'])
    page.locator('id=filesToUpload').set_input_files([])


def storage_restore():
    pessoa = '[{"id": "1659127786998", "name": "Vanilton Pinheiro", "email": "vanilton18@gmail.com", "photo": ""}]'
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context(storage_state={
        "origins": [
            {
                "origin": "https://vanilton18.github.io",
                "localStorage": [{"name": "ng2-webstorage|pessoa", "value": pessoa}],
            }
        ]
    })
    page = context.new_page()
    page.goto("https://vanilton18.github.io/crud-local-storage-angular/")
    print(context.storage_state())
    print(page.locator('div.card').all_inner_texts().__str__());


def test_manipule_localstorage_evaluate():
    pessoa = '[{"id": "1659127786998", "name": "Vanilton Pinheiro", "email": "vanilton18@gmail.com", "photo": ""}]'
    pessoa_dict = json.dumps(pessoa)
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    # Com evaluate script
    page = context.new_page()
    page.goto("https://vanilton18.github.io/crud-local-storage-angular/")
    page.evaluate(f'window.localStorage.setItem("ng2-webstorage|pessoa",{pessoa_dict})')
    # eis o problema
    page.reload()
    print(page.evaluate("window.localStorage.getItem('ng2-webstorage|pessoa');"))
    print(page.locator('div.card').all_inner_texts().__str__())

def globo_esporte_storage():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    # Com evaluate script
    page = context.new_page()
    page.goto("https://google.com")
    context.storage_state(path='storage-gg.json')


if __name__ == '__main__':
    globo_esporte_storage()
    #storage_restore()
    #exemplo_input_file()
    #exemplo_multiple_upload()
    #context_propriedades()
    #contexto_vida()
    #loja_fake_cadastro_usuario()
    #exemplo_confs()
    #exemplo_context_trace()
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
   #exemplo_upload()
   #exemplo_multiple_upload()
   #exemplo_calculadora()
   #exemplo_evaluate_screen_size()
   #exemplo_element_handle()
   #exemplo_keyboard()
   #exemplo_evento_expect_request()
   #test_wait_add_remove_event_listener()
   #exemplo_iframe()
   #exemplo_check_and_radio_buttons()
   #exemplo_save_images()
   #exemplo_loja_fake()
   #exemplo_drag_drop_html5()
   #exemplo_loja_fake()