from behave import *
from locators import *
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time



@step('I click on CreatePoll button from page')
def click_from_home_create_poll(context):
    try:
        context.create_poll.click()
    except NoSuchElementException:
        pass


@when('I open Poll form from navigation bar')
def click_nav_bar_create_poll(context):
    try:
        context.create_poll_from_nav_bar = context.wait.until(
            EC.element_to_be_clickable((
            By.XPATH, Locators.create_poll_navbar_by_xpath)))
    except NoSuchElementException:
        pass
    else:
        context.create_poll_from_nav_bar.click()

@step('type User {name}')
def set_poll_name(context, name):
    context.name_field = context.wait.until(
        EC.visibility_of_element_located((
        By.XPATH, Locators.poll_name_pop_up_by_xpath)))
    context.name_field.send_keys(name)
    time.sleep(1)

@step('type Poll {title}')
def set_poll_title(context, title):
    context.title_field = context.wait.until(
        EC.visibility_of_element_located((
        By.XPATH, Locators.poll_title_pop_up_by_xpath)))
    context.title_field.send_keys(title)

@step('type the Poll {title} in form')
def set_poll_title_in_form(context, title):
    context.title_field = context.wait.until(
        EC.visibility_of_element_located((
            By.ID, Locators.title_field_by_id)))
    context.title_field.send_keys(title)


@step('type a Poll {description} in form')
def set_poll_description_in_form(context, description):
    context.description_field = context.wait.until(
        EC.visibility_of_element_located((
        By.ID, Locators.description_field_by_id)))
    context.description_field.send_keys(description)


@step(u'select first date and time')
def set_first_datetime(context):
    pass


@step(u'select second date and time')
def step_impl(context):
    pass


@step('click save button on the page')
def save_poll_button_home(context):
    context.save_button = context.wait.until(
        EC.element_to_be_clickable((
        By.XPATH, Locators.save_button_home_xpath)))
    context.save_button.click()


@step('click save button in form')
def create_poll_button(context):
    context.save_button = context.wait.until(
        EC.element_to_be_clickable((
        By.XPATH, Locators.save_button_by_xpath)))
    context.save_button.click()

@step('click save name button')
def save_name_button(context):
    context.save_name_button = context.wait.until(
        EC.element_to_be_clickable((
        By.XPATH, Locators.poll_save_button_pop_up_by_xpath)))
    context.save_name_button.click()

@step('click save button to edit')
def save_name_button(context):
    context.save_name_button = context.wait.until(
        EC.element_to_be_clickable((
        By.XPATH, Locators.edit_poll_save_button_xpath)))
    context.save_name_button.click()


@then('Poll is visible on the current page with {title}')
def step_impl(context, title):
    try:
        actual_title = context.wait.until(
            EC.presence_of_element_located((
            By.CLASS_NAME, Locators.actual_title_by_class))
        ).get_attribute("innerHTML")
    except ElementNotVisibleException:
        print("actual title of poll is not found on the page")
    else:
        assert title == actual_title, "AR poll_title != ER poll_title"


@when('I click on My Polls')
def click_my_polls(context):
    try:
        context.my_polls = context.wait.until(
            EC.element_to_be_clickable((
            By.XPATH, Locators.my_polls_by_xpath)))
    except NoSuchElementException:
        print("my_polls button was not found")
    else:
        context.my_polls.click()


@then('I see a list of my polls')
def get_polls_list(context):
    try:
        context.polls_list = context.wait.until(
            EC.visibility_of_element_located((
            By.CLASS_NAME, Locators.polls_list_by_class)))
    except NoSuchElementException:
        print("polls_list was not found")

