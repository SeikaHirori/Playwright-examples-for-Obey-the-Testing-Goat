import pytest

import re
from playwright.sync_api import Page, expect



class Tests_superlists:

    def test_can_start_a_list_and_retrieve_it_later(self, page: Page):
        
        """
            Edith heard about a new online to-do app. 
        She checks out the website.
        """
        page.goto("http://localhost:8000")

        """
            She noticed that the page title and header states "To-Do" lists.
        """
        expect(page).to_have_title(re.compile("To-Do")) # Page title should be "To-Do"


        """
            She is invited to enter a to-do item straight away.
        """



        """    
            She types "Buy peacock feathers" into a text box (Edith's hobby
        is tying fly-fishing lures).
        """


        """
            When she hits enter, the page updates, and now the page lists
        "1: Buy peacock feathers" as an item in a to-do list.

        """
            

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