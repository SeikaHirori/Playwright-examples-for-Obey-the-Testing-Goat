# RFER 01
- Playwright: How to get attribute
    - This is in response to finding the equalivant to Selenium's 'get_attribute'
        - https://www.obeythetestinggoat.com/book/chapter_philosophy_and_refactoring.html#_using_selenium_to_test_user_interactions

>> https://playwright.dev/docs/selectors#quick-guide
> CSS selector
    >> https://playwright.dev/docs/selectors#css-selector

# RFER 02
> Finding by id:
    >> https://playwright.dev/docs/selectors#id-data-testid-data-test-id-data-test-selectors

# RFER 03
> Selector: Finding by element tag name
    >> https://playwright.dev/docs/selectors#role-selector
- Equivalent to Selenium's "find_element_by_tag_name()"

# RFER 04
> assert ".to_have_text()"
    >> https://playwright.dev/python/docs/test-assertions#locator-assertions-to-have-text

# RFER 05
> Locator: .type()
    >> https://playwright.dev/docs/api/class-locator#locator-type

- Equivalent to Selenium's: 
    > input_box.send_keys()

# RFER 06
> Pressing the keyboard's "enter"
    >> https://playwright.dev/docs/api/class-locator#locator-press

- Equivalent to Selenium's:
    > inputbox.send_keys(Keys.ENTER)  

# RFER 07
> Conditional Expression
    >> https://stackoverflow.com/questions/17321138/how-can-i-use-a-conditional-expression-expression-with-if-and-else-in-a-list-c

# RFER 08
- Playwright's:
> .element_handles() 
... equalivent to Selenium's:
> .find_elements_by_tag_name('tr')

>> https://playwright.dev/docs/api/class-elementhandle

- Apparently, Playwright doesn't recommend using elementhandle. Not sure what the alterative is as it only mentions:
> The use of ElementHandle is discouraged, use Locator objects and web-first assertions instead.


# RFER 09

- Playwright's
> .inner_text()
is equal to Selenium's
> .text()

>> https://playwright.dev/docs/api/class-locator#locator-inner-text

# RFER 10
@pytest.mark.django_db
- Error without fixture: 
> E       RuntimeError: Database access not allowed, use the "django_db" mark, or the "db" or "transactional_db" fixtures to enable it.
>> https://stackoverflow.com/a/57692215
>> https://stackoverflow.com/a/66303954

# RFER 11
- QuerySet
>> https://www.fullstackpython.com/django-db-models-query-queryset-examples.html

# RFER 12
Attempting to apply removing whitespace to ALL elements
- Pattern 2:
    >> https://playwright.dev/python/docs/locators#lists

# RFER 13
Removing whitespace in middle of string
>> https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string

# RFER 14
Playwright and Django's LiveServerTestCase
- Main information on setting up
    - Refer to info below on proper setup
    >> https://devblogs.microsoft.com/python/announcing-playwright-for-python-reliable-end-to-end-testing-for-the-web/

- Additional info:
    - Update info about sync_playwright from former to later:
        - Current/new:
            > from playwright.sync_api import sync_playwright
        - Old:
            >  from playwright import sync_playwright 
        >> https://playwright.dev/python/docs/api/class-playwright

- Official Django doc - StaticLiveServerTestCase
    >> https://docs.djangoproject.com/en/2.0/topics/testing/tools/#liveservertestcase

# RFER 15
- Info on error:
> django.core.exceptions.SynchronousOnlyOperation: You cannot call this from an async context - use a thread or sync_to_async.
    >> https://docs.djangoproject.com/en/4.1/topics/async/#sync-to-async
