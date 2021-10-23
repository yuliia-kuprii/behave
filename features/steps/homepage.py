from behave import *
from locators import *
# from features.steps.locators import Locators
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




@when('I see CreatePoll button on the page')
def step_impl(context):
    context.create_poll = context.wait.until(
        EC.visibility_of_element_located((
        By.CLASS_NAME, Locators.create_poll_homepage_by_class)))


@then('the button is displayed on the web-site')
def step_impl(context):
    try:
        context.create_poll.is_displayed()
    except NoSuchElementException:
        pass

