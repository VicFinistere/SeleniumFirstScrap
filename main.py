# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def scrap(urls):
    # On crée une instance du web-driver Firefox et on va sur la page de eBay.fr
    cap = DesiredCapabilities().FIREFOX
    # cap["marionette"] = False
    binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    options = Options()
    # options.set_headless(headless=True)
    options.binary = binary
    driver = webdriver.Firefox(firefox_options=options, capabilities=cap,
                               executable_path="C:\\GeckoDriver\\geckodriver.exe")

    # Go to the main url
    driver.get(urls["main"])

    # Click on the first button (using class name)
    click_on_button_class(driver, "css-cdi241")

    # Go to the tabs page
    driver.get(urls["tabs"])

    # Quit
    driver.quit()

    # En fonction de notre connection et des performance de notre machine il faudra attendre

    # que la page charge avant de passer à la suite


def click_on_button_class(driver, class_name):
    """
    Click on button using class name
    :param driver: Selenium driver
    :param class_name: the name of the button class
    """
    clicked = False
    while not clicked:
        sleep(5)
        if driver.find_element_by_class_name(class_name):
            driver.find_element_by_class_name(class_name).click()
            print(f"button {class_name} is clicked !")
            clicked = True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # URL
    urls = {"main": "https://www.ultimate-guitar.com/",
            "tabs": "https://www.ultimate-guitar.com/user/mytabs"}
    scrap(urls)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
