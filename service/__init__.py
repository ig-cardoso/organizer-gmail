#from authentication import login

from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from getpass import getpass
from time import sleep

from service.teste import *

def login(browser) -> bool:

    print('É necessário informar suas credenciais para se comunicar com a API')
    email = input('\tEmail: ')
    # password = getpass('\tSenha: ')

    login = browser.find_element_by_tag_name('input')
    login.send_keys(email)
    
    # login.click()
    # sleep(10)
    
    #print(password)


def main() -> int:
    # fireFoxOptions = FirefoxOptions()
    # fireFoxOptions.set_headless()
    # browser = Firefox(firefox_options=fireFoxOptions)
    
    browser = Firefox()
    browser.get('http://gmail.com')

    login(browser)
    #browser.quit()

    return 0

if __name__ == '__main__':
    main()