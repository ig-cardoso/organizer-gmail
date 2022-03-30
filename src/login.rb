require 'selenium-webdriver'


def login(driver)
    driver.get('https://gmail.com')
    email = 'igorcardoso99br@gmail.com'
    password = ''

    # search_box_email = driver.find_element(name: 'identifier').send_keys(email)
end


def main
    Selenium::WebDriver::Chrome.driver_path = 'drivers/chromedriver/chromedriver'
    driver = Selenium::WebDriver.for :chrome

    login(driver)

    sleep 30
end


# search_box = driver.find_element(name: 'q')
# search_button = driver.find_element(name: 'btnK')

# search_box.send_keys 'Selenium'
# search_button.click

main


# driver.manage.window.move_to(300, 400)

# driver.quit


# Link: https://github.com/SeleniumHQ/selenium/wiki/Ruby-Bindings
# https://www.selenium.dev/documentation/webdriver/getting_started/first_script/