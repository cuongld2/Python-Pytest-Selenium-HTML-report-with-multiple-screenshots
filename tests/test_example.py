from pytest_bdd import given, when, then, scenario


@scenario(
    "../features/example.feature",
    "Publishing the article",
    example_converters=dict(page1=str, page2=str, page3=str)
)
def test_outlined():
    pass


@given("Go to <page1>")
def goto_page(browser,page1):
    browser.get('https://'+page1)


@when("Go to <page2>")
def goto_page(browser,page2):
    browser.get('https://www.'+page2)


@then("Go to <page3>")
def goto_page(browser,page3):
    browser.get('https://'+page3)