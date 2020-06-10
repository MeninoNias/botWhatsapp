from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self, message, cont):
        self.mensagem = message
        self.cont = cont
        self.grupos_ou_pessoas = ["Name Contato",]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            input('Precione qualquer tecla apos ler o QR code')
            campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            for i in range(0, self.cont):
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                botao_enviar.click()
                time.sleep(0.5)

bot = WhatsappBot('Menssagem', 100)#quantidade de vezes
bot.EnviarMensagens()