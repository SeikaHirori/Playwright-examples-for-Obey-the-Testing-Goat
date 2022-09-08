from xml.sax.xmlreader import Locator
import pytest

import re
from playwright.sync_api import Page, expect, Locator, ElementHandle

import time

class Tests_NewVistor:

    def test_can_start_a_list_and_retrieve_it_later(self, page: Page):
        
        """
            Edith heard about a new online to-do app. 
        She checks out the website.
        """
        page.goto("http://localhost:8000/")

        """
            She noticed that the page title and header states "To-Do" lists.
        """
        expect(page).to_have_title(re.compile("To-Do lists"))

        header_text:Locator = page.locator('role=heading[level=1]') # RFER 3
        expect(header_text).to_have_text(re.compile(r"To-Do list")) # RFER 04


        """
            She is invited to enter a to-do item straight away.
        """
        desired_output_to_do_item:str = 'Enter a to-do item'

        # RFER 01
        locator_input_box:Locator = page.locator('id=id_new_item') # RFER 02

        ### Pythonic way
        assert locator_input_box.get_attribute('placeholder') == desired_output_to_do_item, 'Placeholder should contain "Enter a to-do item"'
        ### Playwright way
        expect(locator_input_box).to_have_attribute(name='placeholder', value=desired_output_to_do_item), 'Placeholder should contain "Enter a to-do item"'

        """    
            She types "Buy peacock feathers" into a text box (Edith's hobby
        is tying fly-fishing lures).
        """
        locator_input_box.type('Buy peacock feathers') # RFER 05

        """
            When she hits enter, the page updates, and now the page lists
        "1: Buy peacock feathers" as an item in a to-do list.

        """
        locator_input_box.press('Enter') # RFER 05 & RFER 06
        time.sleep(1)

        table:Locator = page.locator('id=id_list_table')
        rows:list[ElementHandle] = table.element_handles()
        

        desired_row_text = "1: Buy peakcock feathers"
        


        # Verison 1
        assert True == [True if row.text_content() == desired_row_text else False for row in rows], "New to-do item did not appear in table." #RFER 07

        # Verison 2
        assert desired_row_text in [row.text_content() for row in rows], "New to-do item did not appear in table."

        """
            There is still a text box invitingher to add another item. She
        enters "Use peacock feathers to make a fly" (Edith is very methodical).
        """


        """
            The page updates again, and now shows both items on her list.
        
        """

        """
            Edith wonders whether the site will remember her list. Then she
        sees the site has generate a unique URL for her -- there is some 
        explantory text to that effect.
        """


        """
            She vists that URL - her to-do list is still there.
        """

        """
        Satisfied, she goes back to sleep
        """


        assert "Not complete" == ":'[", f"finish the test!"