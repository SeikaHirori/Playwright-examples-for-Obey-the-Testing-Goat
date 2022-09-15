# Book:
>> https://www.obeythetestinggoat.com/book/part1.harry.html

> Pytest code to run:
pytest -n auto --showlocals --html=report.html --html=report.html --self-contained-html

# Index

- A## - Assertion styles between Python and Playwright
    - Note about the Python's unit testing framework being used here: 
        - The Python assertions are written with Pytest compared to OtTG use of Python's Unittest
    - Example:
        > #RFER 01
        > locator_input_box:Locator = page.locator('id=id_new_item') # RFER 02

        > ####Pythonic way - A01
        > assert locator_input_box.get_attribute('placeholder') == desired_output_to_do_item, 'Placeholder should contain "Enter a to-do item"'
        > ####Playwright way - A01
        > expect(locator_input_box).to_have_attribute(name='placeholder', value=desired_output_to_do_item), 'Placeholder should contain "Enter a to-do item"'

- B## - Selenium code reference from OtTG
    - Example:
        > inputbox = self.browser.find_element_by_id('id_new_item')  
        > self.assertEqual(
        >   inputbox.get_attribute('placeholder'),
        >   'Enter a to-do item'
        > )