from behave import *
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time


@when('I go to Vote section')
def step_impl(context):
    try:
        context.vote_tab = context.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, Locators.vote_tab_by_xpath))
        )
        context.vote_tab.click()
    except NoSuchElementException:
        print("Vote button not found")


@step('I select a nearest day')
def select_day(context):
    context.nearest_day = context.wait.until(
        EC.element_to_be_clickable((
            By.XPATH, Locators.near_day_by_xpath))
    )
    context.week_day_text = context.nearest_day.text
    context.nearest_day.click()


@step('I select {day_time} and {end_time}')
def select_time(context, day_time, end_time):
    context.day_time_option = context.wait.until(
        EC.visibility_of_element_located((
        By.ID, day_time)))
    context.day_time_option.click()
    context.day_time_option_two = context.wait.until(
        EC.visibility_of_element_located((
            By.ID, end_time)))
    context.day_time_option_two.click()



@step('selected time is highlighted')
def step_impl(context):
    css_full_class = context.day_time_option.get_attribute("class")
    assert "selected" in css_full_class, "clicked time is not selected"
    time.sleep(1)


@step('the time is Saved')
def select_time(context):
    context.time_save_button = context.wait.until(
        EC.element_to_be_clickable((
            By.XPATH, Locators.time_save_button_by_xpath))
    )
    context.time_save_button.click()


@step('selected day is highlighted')
def step_impl(context):
    parent = context.nearest_day.find_element_by_xpath("/html/body/app-root/app-poll/div/app-poll-vote/div/ul/li[1]/a/app-poll-vote-date/div")
    css_full_class = parent.get_attribute("class")
    assert "bg-success" in css_full_class, "Filled weekday is not selected"


@step('go to Details section')
def step_impl(context):
    context.details_tab = context.wait.until(
        EC.element_to_be_clickable((
        By.XPATH, Locators.details_tab_by_xpath))
    )
    context.details_tab.click()


@then('charts are displayed')
def step_impl(context):
    try:
        context.all_charts = context.wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, Locators.all_charts_by_class)))
    except ElementNotVisibleException:
        print("Charts are not visible")


# @step('aligned with {day} selected')
# def step_impl(context, day):
#     try:
#         context.chart_day = context.wait.until(
#             EC.visibility_of_element_located((
#             By.XPATH, f'//*[@class="card-title" and text()="{day}"]')))
#         context.chart_day_text = context.chart_day.text
#     except ElementNotVisibleException:
#         print("Chart_day title is not visible")
#     assert context.chart_day_text == context.week_day_text


# @step('set time range from "{start_time}" to "{ending_time}"')
# def step_impl(context, start_time, ending_time):
#     source = context.wait.until(
#         EC.element_to_be_clickable((By.ID, start_time)))
#     context.action_chains.move_to_element(source).click_and_hold().perform()
#     stop = context.wait.until(
#         EC.element_to_be_clickable((By.ID, ending_time)))
#     context.action_chains.move_to_element(stop).release().perform()