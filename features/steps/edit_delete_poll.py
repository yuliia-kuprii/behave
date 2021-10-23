from behave import *
from locators import *
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

@step('open Polls details with {title}')
def step_impl(context, title):
    try:
        context.tile_title_xpath = f"//*[text()='{title}']"
        context.poll_tile = context.wait.until(
            EC.element_to_be_clickable((
            By.XPATH, context.tile_title_xpath)))
    except NoSuchElementException:
        print("No element")
    else:
        context.poll_tile.click()


@step('Delete it')
def step_impl(context):
    try:
        context.delete_button = context.wait.until(
            EC.element_to_be_clickable((
            By.CSS_SELECTOR, Locators.delete_button_by_css)))
    except NoSuchElementException:
        print("No such element")
    else:
        context.delete_button.click()


@step('confirm deletion')
def step_impl(context):
    try:
        context.wait.until(EC.alert_is_present())
        context.alert = context.browser.switch_to.alert
        context.alert.accept()
    except TimeoutException:
        print("no alert")

@then('poll\'s {title} is not in the list')
def step_impl(context, title):
    try:
        context.wait.until(
            EC.invisibility_of_element_located((
            By.XPATH, context.tile_title_xpath)))
    except Exception:
        print("Poll is visible in the list and not deleted")

@step('open edit mode')
def step_impl(context):
    try:
        context.edit_button = context.wait.until(
            EC.element_to_be_clickable((
            By.CSS_SELECTOR, Locators.edit_button_by_css)))
        context.edit_button.click()
    except NoSuchElementException:
        print("No such element")



@step('change to {new_title}')
def step_impl(context, new_title):
    context.title_field = context.wait.until(
        EC.visibility_of_element_located((
        By.ID, Locators.title_field_by_id)))
    context.title_field.clear()
    context.title_field.send_keys(new_title)


@then('poll has a new {new_title}')
def step_impl(context, new_title):
    context.actual_edited_title = context.wait.until(
        EC.visibility_of_element_located((
        By.CLASS_NAME, Locators.actual_title_by_class))
    )
    print(context.actual_edited_title.text)
    assert context.actual_edited_title.text == new_title.upper(), "titles are not the same"
