# Post-reflection blog
    > ***TBA***

# Book used
- Obey the Testing Goat (OtTG)
    > https://www.obeythetestinggoat.com/book/part1.harry.html

# Objectives of Repository
- Instead of using Selenium and Python's unittest, Playwright and Pytest are used instead while following OtTG.
- This repo provides reference/ examples to how Playwright and Pytest could subsitute Selenium and Python's unittest.
    - ***DISCLAIMER***: The code I wrote while following the book may have better alternatives. I recommend looking at the official Playwright documentation to confirm the needed tools.
    
- Chapters finished so far:
    - Part 1: The Basics of TDD and Django

# Index

- RFER
    - "# RFER XX" seen in the code is used as a reference to documentation and materials used to help write the code.

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
