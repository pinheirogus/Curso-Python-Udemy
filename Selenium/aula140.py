import selenium.common.exceptions
from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir=C:\Users\Gustavo\AppData\Local\Google\Chrome\User Data\Selenium')
        self.options.add_argument("--disable-extensions")
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options = self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except selenium.common.exceptions.NoSuchElementException as error:
            try:
                btn_menu = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div > div.d-flex.flex-justify-between.flex-items-center > div.d-flex.flex-items-center > button > svg')
                btn_menu.click()
                btn_sign_in = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu.HeaderMenu--logged-out.position-fixed.top-0.right-0.bottom-0.height-fit.position-lg-relative.d-lg-flex.flex-justify-between.flex-items-center.flex-auto > div.d-lg-flex.flex-items-center.px-3.px-lg-0.text-center.text-lg-left > div.position-relative.mr-3 > a')
                btn_sign_in.click()
            except Exception as error:
                print('Erro ao clicar em sign in: ', error)
        except Exception as error:
            print('Erro ao clicar em sign in: ', error)

    def login(self):
        try:
            campo_login = self.chrome.find_element_by_id('login_field')
            campo_login.send_keys('gstvdm@gmail.com')

            campo_senha = self.chrome.find_element_by_id('password')
            campo_senha.send_keys('4347442w')

            btn_login = self.chrome.find_element_by_name('commit')
            btn_login.click()
            sleep(10)
        except Exception as error:
            print('Erro ao fazer login.', error)

    def logout(self):
        try:
            btn_logout = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            btn_logout.click()
        except Exception as error:
            print('Erro ao fazer logout.', error)

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > img')
            perfil.click()
            sleep(10)
        except Exception as error:
            print('Erro ao clicar no perfil', error)

    def verifica_usuario(self, usuario ):
        profile_link = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    print('Google Chrome aberto com sucesso')

    chrome.clica_sign_in()
    print('Botão de sign in clicado com sucesso')
    chrome.login()
    print('Login realizado com sucesso')
    sleep(5)
    chrome.clica_perfil()
    print('Perfil clicado com sucesso')
    chrome.verifica_usuario('Gstvdm')
    print('Usuario verificado com sucesso')
    chrome.logout()
    print('Logout realizado com sucesso')

    sleep(3)
    chrome.sair()