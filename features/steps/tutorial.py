from behave import *
from pymacaroons.utils import equals
from selenium import webdriver


@given('we have behave installed, and chrome launched')
def step_impl(context):
    context.driver = webdriver.Chrome()
    pass

@when ('we implement a test, visit a page')
def step_impl(context):
    context.driver.get("https://www.google.com")
    assert True is not False

@then('behave will test for me and page is opened!')
def step_impl(context):
    current_url = context.driver.current_url
    assert equals(current_url, "https://www.google.com/") is True
    assert context.failed is False
