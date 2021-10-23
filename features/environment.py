from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


def before_all(context):
    driver_choices = {
        "FF": webdriver.Firefox(executable_path='/Users/kupriyandrey/PROJECTS/behave/Webdrivers/FF/geckodriver'),
        # "Chrome": webdriver.Chrome('/Users/kupriyandrey/PROJECTS/behave/Webdrivers/Chrome/chromedriver'),
        # "Safari": webdriver.Safari()
    }
    context.browser = driver_choices["FF"]
    context.browser.maximize_window()
    context.browser.implicitly_wait(10)


def before_feature(context, url):
    context.browser.get("https://polls-8f41b.web.app/#/")


def before_step(context, sec):
    context.wait =WebDriverWait(context.browser, 10)
    context.action_chains = ActionChains(context.browser)


def after_all(context):
    context.browser.quit()


