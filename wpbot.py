from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "teste!!!!!!"
        self.grupos = ["Cesar"]
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        #<span dir="auto" title="Anotação" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Anotação</span>
        #<div tabindex="-1" class="p3_M1"><div tabindex="-1" class="_1UWac _1LbR4"><div class="_2vbn4" style="visibility: visible;">Type a message</div><div title="Type a message" role="textbox" class="_13NKt copyable-text selectable-text" contenteditable="true" data-tab="10" dir="ltr" spellcheck="true"></div></div></div>
        #<span data-testid="send" data-icon="send" class=""><svg viewBox="0 0 24 24" width="24" height="24" class=""><path fill="currentColor" d="M1.101 21.757 23.8 12.028 1.101 2.3l.011 7.912 13.623 1.816-13.623 1.817-.011 7.912z"></path></svg></span>
        self.driver.get('https://web.whatsapp.com')
        print('Chegou aqui')
        time.sleep(30)
        print('Chegou aqui 2')
        for grupo in self.grupos:
            print('Chegooouuu')
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            print('Chegou aqui 3')
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-testid='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()