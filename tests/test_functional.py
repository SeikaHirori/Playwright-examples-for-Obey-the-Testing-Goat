from cmath import exp
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

        ### Pythonic way - 01
        assert locator_input_box.get_attribute('placeholder') == desired_output_to_do_item, 'Placeholder should contain "Enter a to-do item"'
        ### Playwright way - 01
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
        rows:list[ElementHandle] = table.element_handles() # RFER 08
        # rows:list[ElementHandle] = table.locator('tr').locator('td') # Doesn't work
        

        desired_row_text_1:str = "1: Buy peacock feathers"

        # # Verison 1
        # assert True in [True if row.text_content() == desired_row_text_1 else False for row in rows], f"New to-do item did not appear in table. Contents were:\n{table.inner_text()}" #RFER 07
        

        # Verison 2 - I DID THIS BEFORE I SAW IT IN THE BOOK WOOT

        ### Pythonic Way - 02
        assert desired_row_text_1 in [row.inner_text() for row in rows], f"New to-do item did not appear in table. Contents were:\n {table.inner_text()}" # RFER 09
        ### Playwright Way - 02
        expect(table).to_have_text(desired_row_text_1)

        desired_row_text_2:str = '2: Use peacock feathers to make a fly'
        assert desired_row_text_2 in [row.inner_text() for row in rows]

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