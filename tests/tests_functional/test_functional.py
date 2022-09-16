import pytest

#### Selenium style - B00: Import libary
# from selenium import webdriver 
####

from playwright.sync_api import Page, expect, Locator, ElementHandle
import re

import time

import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import sync_playwright

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError




MAX_WAIT:int = 10

class Tests_NewVistor(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls) -> None: # RFER 14
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true" # RFER 17 - LOOK AT THIS
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.firefox.launch()
    
    @classmethod
    def tearDownClass(cls) -> None: # RFER 14
        cls.browser.close()
        cls.playwright.stop()
        super().tearDownClass()

    def wait_for_row_in_list_table(self, row_text:str, page:Page): # Page is needed for Playwright; It isn't needed for Selenium SO it's parameter would be "wait_for_row_in_list_table(self, row_text:str)"
        #### Selenium style - B07
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')  
        # self.assertIn(row_text, [row.text for row in rows])
        ####
        start_time = time.time()
        while True: 
            try:
                table:Locator = page.locator('id=id_list_table')
                        
                # String way
                rows:str = table.inner_text() # RFER 08 # Stores whole list in a string that also contains "\n"
                
                #### Pythonic Way - A04.1
                assert row_text in rows
                #### Playwright Way - A04: This is similar to the Pythonic Way - A04.01
                expect(table).to_contain_text(row_text)
                
                
                #### Pythonic Way - A04.2: Using rows_list:list[str] is more precise than rows:str
                # List way
                rows_list:list[str] = table.inner_text().splitlines()
                assert row_text in rows_list, f"New to-do item did not appear in table. Contents were:\n{table.inner_text()}" # RFER 09

                return
            except (AssertionError, PlaywrightTimeoutError) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def test_can_start_a_list_and_retrieve_it_later(self):

        #### Selenium style - B01
        # browser = webdriver.Firefox()
        ####

        page = self.browser.new_page()


        """
            Edith has heard about a cool new online to-do app. She goes to check out its homepage
        """
        #### Selenium style - B02:
        # self.browser.get(self.live_server_url)
        ####

        page.goto(self.live_server_url)



        """
            She noticed that the page title and header states "To-Do" lists.
        """
        #### Selenium style - B03
        # self.assertIn('To-Do', self.browser.title)
        # header_text = self.browser.find_element_by_tag_name('h1').text  
        # self.assertIn('To-Do', header_text)
        ####

        expect(page).to_have_title(re.compile("To-Do lists"))
        header_text:Locator = page.locator('role=heading[level=1]') # RFER 3
        expect(header_text).to_have_text(re.compile(r"To-Do list")) # RFER 04


        """
            She is invited to enter a to-do item straight away.
        """
        #### Selenium style - B04
        # inputbox = self.browser.find_element_by_id('id_new_item')  
        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'Enter a to-do item'
        # )
        ####

        desired_output_to_do_item:str = 'Enter a to-do item'

        # RFER 01
        locator_input_box:Locator = page.locator('id=id_new_item') # RFER 02

        #### Pythonic way - A01
        assert locator_input_box.get_attribute('placeholder') == desired_output_to_do_item, 'Placeholder should contain "Enter a to-do item"'
        #### Playwright way - A01
        expect(locator_input_box).to_have_attribute(name='placeholder', value=desired_output_to_do_item), 'Placeholder should contain "Enter a to-do item"'



        """    
            She types "Buy peacock feathers" into a text box (Edith's hobby
        is tying fly-fishing lures).
        """
        #### Selenium style - B05
        # inputbox.send_keys('Buy peacock feathers')  
        ####

        locator_input_box.type('Buy peacock feathers') # RFER 05



        """
            When she hits enter, the page updates, and now the page lists
        "1: Buy peacock feathers" as an item in a to-do list.

        """
        #### Selenium style - B06
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)
        # self.wait_for_row_in_list_table('1: Buy peacock feathers')
        ####

        locator_input_box.press('Enter') # RFER 05 & RFER 06
        time.sleep(1)

        desired_row_text_1:str = "1: Buy peacock feathers"
        self.wait_for_row_in_list_table(desired_row_text_1, page)



        """
            There is still a text box invitingher to add another item. She
        enters "Use peacock feathers to make a fly" (Edith is very methodical).
        """
        #### Selenium style - B08
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # inputbox.send_keys('Use peacock feathers to make a fly')
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)
        ####
        locator_input_box:Locator = page.locator('id=id_new_item') # RFER 02
        locator_input_box.type('Use peacock feathers to make a fly')
        locator_input_box.press('Enter')
        time.sleep(1)

        """
            The page updates again, and now shows both items on her list.
        
        """
        #### Selenium style - B0
        # self.wait_for_row_in_list_table('1: Buy peacock feathers')
        # self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        ####

        self.wait_for_row_in_list_table(desired_row_text_1, page)
        desired_row_text_2:str = '2: Use peacock feathers to make a fly'
        self.wait_for_row_in_list_table(desired_row_text_2, page)


        """
            Edith wonders whether the site will remember her list. Then she
        sees the site has generate a unique URL for her -- there is some 
        explantory text to that effect.
        """
        #### Selenium style - B0
        
        ####



        """
            She vists that URL - her to-do list is still there.
        """
        #### Selenium style - B1
        
        ####



        """
        Satisfied, she goes back to sleep
        """
        #### Selenium style - B1
        
        ####


        page.close()
        assert "Not complete" == ":'[", f"finish the test!"
